"""
Write a Python program to find the second smallest number in a list.
"""

"""
1)) Take in the number of elements and store it in a variable.
2)) Take in the elements of the list one by one.
3)) Sort the list in ascending order.
4)) Print the last element of the list.
"""

li = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    li.append(elem) 
li.sort() 

print("The sorted list: ", li) 
print("The second smallest value of this list: ",li[1])
