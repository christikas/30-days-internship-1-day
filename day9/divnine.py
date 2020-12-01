# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:39:53 2020

@author: kristika
"""


my_list = [12, 45, 54, 39, 81, 339, 108,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 9 == 0), my_list))

# display the result
print("Numbers divisible by 9 are",result)