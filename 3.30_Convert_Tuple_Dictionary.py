"""
Write a Python program to convert a list of tuples into a dictionary.
"""
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}


for a, b in l:
    # Use 'setdefault' to create an empty list in the dictionary 'd' for the key 'a' if it doesn't exist.
    # Then, append the value 'b' to the list associated with key 'a'.
    d.setdefault(a, []).append(b)


print(d) 
