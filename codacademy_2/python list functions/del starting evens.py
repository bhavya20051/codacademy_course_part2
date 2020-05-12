# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:08:54 2020

@author: bhavy
"""


#Write your function here
def delete_starting_evens(lst):
  for lst[0] in lst:
    if lst[0]%2==0:
      lst.remove(lst[0])
  return lst

      
  
    

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#on second statement, should return empty list but returns[10]