# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:30:01 2018

@author: staie
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


unique =[i for i in a if i in b]
print (unique)

import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]


x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0]

print (customlist)

 