
"""
    https://www.codewars.com/kata/5a62da60d39ec5d947000093/train/python
"""
def findSquares(m, n):
    total_squares = 0

    for i in range(1, n + 1):
        total_squares += (m - i + 1) * (n - i + 1)

    return total_squares

rectangulo_1 = findSquares(3, 2)