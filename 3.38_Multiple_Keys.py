"""
Write a Python program to check multiple keys exists in a dictionary. 
"""

student = {'name': 'chinmayee',  'course': 'python','city': 'ahmedabad'}


print(student.keys() >= {'course', 'name'})


print(student.keys() >= {'name', 'chinmayee'})


print(student.keys() >= {'city', 'name'}) 
