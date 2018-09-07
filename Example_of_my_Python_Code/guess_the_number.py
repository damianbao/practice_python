# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:57:17 2018

@author: staie
"""

import random as r

solution = r.randint (1,10)
guess = int(input ('Please guess a number: '))


while guess != solution:
    if guess < solution:
        print ('Too low!!')
        guess = int(input ('Please guess a number: '))
        
    if guess > solution:
        print ('Too High!!')
        guess = int(input ('Please guess a number: '))
        
    if guess == solution:
        print('You did it!!!')
        break