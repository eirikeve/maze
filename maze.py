# maze.py
# Written by Eirik Vesterkjær, 2017
#
# Maze generator
# Uses a randomized Prim's Algorithm to create a MST of cells.
# Can be used wiht a CLI or in other projects

import random
import sys


"""
Prints the maze elements
@arg maze: 2d array
"""
def printMaze(maze):
    for row in maze:
        for elem in row:
            print(elem, end=" ")
        print()

"""
Prints the maze prettier.
For use with finished mazes, since it assumes elements are only 0 or 1.
@arg maze: 2d array
"""
def printFinishedMaze(maze):
    for row in maze:
        for elem in row:
            if (elem):
                print("[]", end="")
            else:
                print("  ", end="")
        print()

"""
Returns a listing of coordinates of cells representing REMOVABLE_WALL around (x,y)
@arg maze: 2d array A[x][y]
@arg x: x-index of a cell
@arg y: y-index of a cell
@return: list of coordinate tuples (x,y)
"""
def getWallsAround(maze, x, y):
    REMOVABLE_WALL = 2
    if not ((0 <= x < len(maze)) and (0 <= y < len(maze[0]))):
        raise IndexError
    around = []
    for i in range(max(x - 1, 0), min(x + 2, len(maze))):
        for j in range(max(y-1, 0), min(y + 2, len(maze[i]))):
            if (maze[i][j] == REMOVABLE_WALL):
                around.append((i,j))
    return around

"""
Uses a randomized Prim's MST algorithm to create a maze.
@arg xlength: x-length of return maze[x][y]
@arg ylength: y-length of return maze[x][y]
@arg random_seed: int seed for RNG
@return: 2d maze[xlength][ylength] where 1 is a wall, and 0 is a path
"""
def getMaze(xlength, ylength, random_seed):
    # A constant seed will always give the same maze
    random.seed(random_seed)
    # Definitions:
    # non-visited cell
    NON_VISITED_CELL = 0
    # -1 = visited cell or removed wall
    VISITED_CELL = -1
    # 2 = removable wall
    REMOVABLE_WALL = 2
    # 1 = non-removable wall
    NON_REMOVABLE_WALL = 1
    
    # Create a grid of zeroes and ones. Every (non-visited) path cell is surrounded by walls
    maze = [[int(not (((i % 2) * (j % 2)) == 1))  for i in range(ylength)] for j in range(xlength)]

    if xlength < 2 or ylength < 2:
        return maze

    # Make edges of array into walls
    for x in range(xlength):
        maze[x][0] = NON_REMOVABLE_WALL
        maze[x][-1] = NON_REMOVABLE_WALL
    for y in range(ylength):
        maze[0][y] = NON_REMOVABLE_WALL
        maze[-1][y] = NON_REMOVABLE_WALL
    
    #Don't include edges - we do not want to remove those edges
    for x in range(1, xlength - 1):
        for y in range(1, ylength - 1):
            #Mark wall.
            if maze[x][y] and ((x%2) == 1 or (y%2) == 1) and not (((x % 2) * (y % 2)) == 1):
                maze[x][y] = REMOVABLE_WALL
            # Cell. Add set to this

    # Stack for MST creation: Coordinates of walls adjacent to visited cells
    walls_stack = []


    # Start MST at (1,1)
    maze[1][1] = VISITED_CELL
    for w in getWallsAround(maze, 1, 1):
        walls_stack.append(w)


    while walls_stack.__len__():
        # Randomly get get a wall that has not yet been removed
        i = random.randint(0, walls_stack.__len__() - 1)
        wall = walls_stack.pop(i)

        x = wall[0]
        y = wall[1]

        # If there are any cells we can visit by removing this wall, then remove it
        unvisitedAroundWall = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                # We can visit this cell by removing the wall. So
                if maze[i][j] == NON_VISITED_CELL:
                    # Count the number of unvisited cells
                    unvisitedAroundWall += 1
                    # Mark this cell as visited, and add its adjacent walls to the stack
                    maze[i][j] = VISITED_CELL
                    for w in getWallsAround(maze, i, j):
                        walls_stack.append(w)
        # There are cells we can visit through this wall, so we remove it
        if (unvisitedAroundWall):
            maze[x][y] = VISITED_CELL


    # Make maze into wall (1) / path (0) for printing / return
    for x in range(xlength):
        for y in range(ylength):
            if maze[x][y] == -1 or maze[x][y] == 3 or maze[x][y] == 0:
                maze[x][y] = NON_VISITED_CELL
            else:
                maze[x][y] = NON_REMOVABLE_WALL
    return maze




# If running directly from CLI
if __name__ == "__main__":
    # Only width and height parameters
    if 2 < len(sys.argv):
        # Corresponds to x dimension
        height = int(sys.argv[1])
        # Corresponds to y dimension
        width  = int(sys.argv[2])
        # Seed for randomization
        ran_seed = 0 if len(sys.argv) < 4 else sys.argv[3]
        # Print to CLI
        printFinishedMaze( getMaze(height, width, ran_seed) )
    else:
        print("Error! Call using: python maze.py height width [random seed]")

