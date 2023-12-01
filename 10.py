"""
    https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python
"""

def lowercase_count(strng):
    data_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cont=0
    for i in strng:
        if i in data_set:cont+=1
    return cont
print(lowercase_count('abcd'))