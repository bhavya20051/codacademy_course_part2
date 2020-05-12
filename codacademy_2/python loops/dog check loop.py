# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:44:46 2020

@author: bhavy
"""

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog==dog_breed_I_want:
    break
print("They have the dog I want!")

