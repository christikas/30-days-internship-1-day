# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:22:36 2020

@author: kristika
"""


class Accident(Exception):
	def _init_(self, message):
		self.message = message
	def print_exception(self):
		print("Our custom exception is...", self.message)
		
try:
	raise Accident("here")
except Accident as a:
	a.print_exception()