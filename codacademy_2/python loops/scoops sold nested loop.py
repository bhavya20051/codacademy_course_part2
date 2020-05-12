# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:01:24 2020

@author: bhavy
"""

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold=0
for location in sales_data:
  print(location)
  for number in location:
    scoops_sold+= number
print(scoops_sold)
  
