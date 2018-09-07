# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:39:22 2018

@author: staie
"""

import random

roll = input ('Would you like to roll the dice? (y or n)')

while roll == 'y':
    result = random.randint(1,20)
    print ("And your dice roll is: " + str(result))
    roll = input ('Would you like to play again? (y or n) ' )
    if roll != 'y':
        break
     
 