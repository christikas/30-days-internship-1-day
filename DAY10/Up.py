# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:17:30 2020

@author: kristika
"""


import re
def text_match(text):
        patterns = '^[A-Z]'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy DOG."))
print(text_match("Python_Exercises_1"))