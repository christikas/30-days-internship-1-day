# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:09:42 2020

@author: kristika
"""


def division(first, second):
	try:
		result = first / second
		print(result)
	except Exception as e:
		print(e)
		
def calculation():
	try:
		first = int(input())
		second = int(input())
		division(first, second)
	except Exception as e:
		print("You can't put anything but integer numbers")
		calculation()
#call a function
calculation()