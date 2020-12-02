# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:12:12 2020

@author: kristika
"""


test_string = "I am  christika from saveetha engineering college"

  
# printing original string 

print ("The original string is : " +  test_string) 

  
# using split() 
# to count words in string 

res = len(test_string.split()) 

  
# printing result 

print ("The number of words in string are : " +  str(res))