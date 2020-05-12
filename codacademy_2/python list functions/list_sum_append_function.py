#Write your function here
#sum function:
def append_sum(lst):
  appended = lst.append(lst[-2] + lst[-1])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2,]))