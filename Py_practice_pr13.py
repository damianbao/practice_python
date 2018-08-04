# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:20:45 2018

@author: rdsta
"""

# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number
# in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
a,b = 0,1
fib = []
num = int(input("What number Fibonacci number do you want? "))



for i in range(num):
    a,b = b, a+b
    fib.append(b)
print (fib)
print (len(fib))





def fibonnaci (num):
    sol = (((1.6180339**num - (-0.6180339)**num))/2.236067977)
    print (sol)
    
print (fibonnaci(num))
        
        
        