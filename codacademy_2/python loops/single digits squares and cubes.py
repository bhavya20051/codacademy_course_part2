# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:12:43 2020

@author: bhavy
"""


single_digits=[0,1,2,3,4,5,6,7,8,9]
squares=[]
for number in single_digits:
  print(number)
  squares.append(number**2)
print(squares)
cubes=[number**3 for number in single_digits]
print(cubes)