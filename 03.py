
"""
   https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
   Create a function that takes an integer as an argument and
   returns "Even" for even numbers or "Odd" for odd numbers.
"""
def even_or_odd(number):
    if number % 2 == 0:return 'Even' 
    return 'Odd'

print(even_or_odd(7))