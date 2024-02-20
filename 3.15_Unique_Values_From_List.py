"""
Write a Python program to get unique values from a list
"""

list_inp=[500, 100, 500, 200, 750, 120, 750, 250] 

res_list=[]

for item in list_inp: 
    if item not in res_list: 
        res_list.append(item) 

print("Unique elements of the list using append():\n")    
for item in res_list: 
    print(item) 
