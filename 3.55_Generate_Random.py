"""
How will you set the starting value in generating random numbers?
"""

import random 
for i in range(5):
    
    random.seed(0)
    print(random.randint(1, 1000))  
