"""
"""
import numpy        
def roll_points():
    """Creates a number to use as a stat following the requirements 
       for a 5e dnd character

       Returns:
       A int
    """
    points = [numpy.random.randint(1, 6) for _ in range(4)]
    lowest = min(points)
    points.remove(lowest)
    return sum(points)
        