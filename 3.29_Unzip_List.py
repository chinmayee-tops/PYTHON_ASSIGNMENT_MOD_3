"""
Write a Python program to unzip a list of tuples into individual lists.
"""
l = [(1, 2), (3, 4), (8, 9)]

"""Use the 'zip' function with the '*' operator to unpack and zip the tuples.
This creates new tuples where the first elements from the original tuples are combined into one tuple,
and the second elements from the original tuples are combined into another tuple.
"""
result = list(zip(*l))
print(result)
