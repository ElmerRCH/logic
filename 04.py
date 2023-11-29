"""
    https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
    In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
    Years divisible by 4 are leap years,
    but years divisible by 100 are not leap years,
    but years divisible by 400 are leap years.
    Tested years are in range 1600 ≤ year ≤ 4000.
"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):return True
    return False
print(is_leap_year(2000))
