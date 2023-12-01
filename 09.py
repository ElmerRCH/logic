"""
    https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
"""

def add_length(str_):
    palabras = str_.split()
    return [f"{palabra} {len(palabra)}" for palabra in palabras]

print(add_length("apple ban"))
