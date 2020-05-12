# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:31:10 2020

@author: bhavy
"""


def divisible_by_ten(nums):
  lst2=[]
  i=0
  for number in nums:
    if number%10==0:
      lst2.append(number)
  return len(lst2)
  

    
    
      
 
nums=[20, 25, 30, 35, 40] 

#Uncomment the line below when your function is done
print(divisible_by_ten(nums))