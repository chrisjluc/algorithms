"""This module contains utility functions for the geometry module.
"""

def dist_squared (a, b):
    """Returns the squared euclidean distance between points a and b.
    """
    return sum(map(lambda (x,y): (x-y)**2, zip(a, b)))