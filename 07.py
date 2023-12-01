"""
    https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python
"""

def isDigit(s):
    s = s.strip()

    return (s[0] == '-' and s[1:].isdigit()) or s.isdigit()


print(isDigit("-3.23"))
