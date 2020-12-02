# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:03:05 2020

@author: kristika
"""


import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))