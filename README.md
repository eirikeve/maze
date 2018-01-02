# maze
Maze generator using a randomized Prim's algorithm.  
Can output to a command line interface, or can be included in other projects.  
Written in Python 3.

# Usage
If using directly from terminal, call: `python maze.py height width [random seed]`

Otherwise, use `getMaze(xlength, ylength, random_seed)`

# Example input
```bash
me@my-computer:~/Folder$ python maze.py 21 21 10
[][][][][][][][][][][][][][][][][][][][][]
[]      []      []          []  []  []  []
[]  [][][][][]  []  [][][][][]  []  []  []
[]                              []  []  []
[]  [][][]  []  [][][]  [][][][][]  []  []
[]      []  []      []                  []
[]  [][][]  []  []  []  []  [][][]  []  []
[]  []      []  []  []  []  []      []  []
[]  []  [][][]  [][][][][]  [][][]  []  []
[]  []  []              []  []      []  []
[]  [][][][][]  []  [][][][][]  []  [][][]
[]      []      []      []      []      []
[]  [][][][][]  []  [][][][][]  [][][][][]
[]      []  []  []          []      []  []
[]  [][][]  [][][]  []  []  [][][][][]  []
[]              []  []  []              []
[][][]  []  []  [][][]  [][][][][][][][][]
[]      []  []      []                  []
[]  []  [][][][][][][]  []  [][][]  []  []
[]  []      []          []      []  []  []
[][][][][][][][][][][][][][][][][][][][][]
```
