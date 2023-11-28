
"""
    https://www.codewars.com/kata/62b3e38df90eac002c7a983f/train/python
"""
def findSquares(m, n):
    total_squares = 0

    for i in range(1, n + 1):
        total_squares += (m - i + 1) * (n - i + 1)
    
    return total_squares

rectangulo_1 = findSquares(3, 2)