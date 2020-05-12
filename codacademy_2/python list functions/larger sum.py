# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:45:51 2020

@author: bhavy
"""


#Write your function here
def larger_sum(lst1,lst2):
  sum1=0
  for number in lst1:
    sum1+=number
  sum2=0
  for number in lst2:
    sum2+=number
  if sum2>sum1:
    return lst2
  else:
    return lst1
  
  


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))