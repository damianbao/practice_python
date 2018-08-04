# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:30:01 2018

@author: staie
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print ([ x for x in b if x not in a] + [x for x in a if x not in b])