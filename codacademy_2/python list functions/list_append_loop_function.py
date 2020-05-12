#Write your function here
#uses loops to append the sum of last two elements in a list three times
#sum function:
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-2] + lst[-1])
    return lst

    

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2, 5]))