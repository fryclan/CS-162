"""
"""
import numpy

debug = 0

def roll_points():
    """Creates a number to use as a stat following the requirements 
       for a 5e dnd character

       Returns:
       A int
    """
    points = [numpy.random.randint(1, 7) for _ in range(4)]
    lowest = min(points)
    points.remove(lowest)
    return sum(points)

counter = 0

while debug == 1:
   counter += 1
   if roll_points() == 18:
      break
   else:
      continue
print(counter)
