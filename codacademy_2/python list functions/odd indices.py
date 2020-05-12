# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:31:29 2020

@author: bhavy
"""


#Write your function here
def odd_indices(lst):
    odd=[]
    for index in range(1,len(lst),2):
      odd.append(lst[index])
    return odd
    

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))