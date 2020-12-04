# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:34:02 2020

@author: kristika
"""


numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False

evenNums = filter(even_numbers, numbers)
print('Even Numbers are:')
for num in evenNums:
    print(num)