# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:05:49 2020

@author: kristika
"""


import re
def text_match(text):
        patterns = '\w*a.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("I can able to find."))
print(text_match("about me."))