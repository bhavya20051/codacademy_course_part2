# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:00:57 2020

@author: bhavy
"""
#using list comprehension
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster =[number for number in heights if number>161]
print(can_ride_coaster)

#not using list comprehension
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster=[]

for number in heights:
    if number>161:
        can_ride_coaster.append(number)
print(can_ride_coaster)


  
  