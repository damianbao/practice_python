# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:15:08 2018

@author: staie
"""

import random
answer = random.randint(1,9)
guess  = input ('please guess a number between 1 and 9:')


while guess != answer:
    if guess == answer:
        print ('You nailed it!')
        answer = random.randint(1,9)
        guess  = input ('please guess a number between 1 and 9:')
        
    elif guess != answer:
        print ('you got it wrong :( ')
        print ('the answer was',answer)
        answer = random.randint(1,9)
        guess  = input ('please guess a number between 1 and 9:')
        
    if guess == 'quit':
        break    
        