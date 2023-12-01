"""
    https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python
"""

def is_digit(s):
    if type(s) == str:
        return s.isdigit()
    elif type(s) == int:
        return True
    else:
        return False

print(is_digit('b'))
