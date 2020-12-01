# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:21:36 2020

@author: kristika
"""


dictionary = {"a":0, "b":1, "c":2}

try:
	value = dictionary[input()]
except KeyError:
	print("An error has occured!")
else:
	print("Everything's fine!")
finally:
	print("It's finally over!!!")