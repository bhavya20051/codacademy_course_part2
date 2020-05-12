# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:10:59 2020

@author: bhavy
"""


#Write your function here


def over_nine_thousand(lst):
  t = [0]
  while sum(t) < 9000:
   t.append(lst[0])
   del lst[0]  
  return sum(t)



#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))