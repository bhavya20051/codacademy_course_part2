# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:07:22 2020

@author: bhavy
"""


#Write your function here
def same_values(lst1,lst2):
   index1=[]
   for index in range(len(lst1)):
    if lst1[index]==lst2[index]:
      index1.append(index)
   return index1



#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))