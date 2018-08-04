# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:07:47 2018

@author: staie
"""
#Write a program that takes a list of numbers (for example, 
#a = [5, 10, 15, 20, 25]) and makes a new list of only the first 
#and last elements of the given list. For practice, write this 
#code inside a function.

import random as r

b=r.sample(range(20),10)
print (b)

def to_the_extremes (a):
    new_list  = [(a[0],a[-1])]
    print (new_list)


to_the_extremes(b)