# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:15:26 2020

@author: bhavy
"""


#Write your function here
def max_num(nums):
    maximum=nums[0]
    for number in nums:
      if number>maximum:
        maximum=number
    return maximum
   
      

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))