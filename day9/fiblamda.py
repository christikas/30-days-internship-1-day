# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:36:34 2020

@author: kristika
"""


def fibonacci(count):
   listA = [0, 1]

   any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))

   return listA[:count]

print(fibonacci(8))