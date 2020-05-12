# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:53:00 2020

@author: bhavy
"""


#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))