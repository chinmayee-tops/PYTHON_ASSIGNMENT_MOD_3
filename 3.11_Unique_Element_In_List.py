"""
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
"""

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,4,3,5,5,5])) 
