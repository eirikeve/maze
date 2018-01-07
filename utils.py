import argparse

def check_positive(value):
    """ Check if value is a positive integer, if not raise exception to argparse"""
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not an int value" % value)
    else:
        if value < 0:
            raise argparse.ArgumentTypeError("%s is not a positive int value" % value)
    finally:
        return value