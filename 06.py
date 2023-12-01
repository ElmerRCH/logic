"""
    https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python
    Given a point in a Euclidean plane (x and y), return the quadrant the point exists in:
    1, 2, 3 or 4 (integer). x and y are non-zero integers
    therefore the given point never lies on the axes.
"""
def quadrant(x, y):
    
    if x > 0 and y > 0:return 1 
    if x < 0 and y > 0:return 2
    if x < 0 and y < 0:return 3 
    if x > 0 and y < 0:return 4 
    
print(quadrant(5,10))
