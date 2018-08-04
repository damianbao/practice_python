# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:15:31 2018

@author: staie
"""

play_again = 'y'
while play_again == 'y':
    choice1 = int (input ('Player One! \n Choose your weapon!!!\n Enter 1 for rock.\n 2 for paper, \n Or 3 for scissors: '))
    choice2 = int (input ('Player Two! \n Choose your weapon!!!\n Enter 1 for rock.\n 2 for paper, \n Or 3 for scissors: '))


#3v2
#2v1
#1v3



    if choice1 == choice2:
        print ('You both chose the same Weapon. Mutual Destruction!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
        if play_again == 'y':
            continue
        if play_again != 'y':
            print('Thanks for playing')
            break
        
    if choice1 == 3 and choice2 == 2:
        print ('Player one is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
       
              
            
    elif choice1 == 3 and choice2 == 1:
        print ('Player two is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
        
    elif choice2 == 1 and choice1 == 2:
        print ('Player one is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
        
    elif choice2 == 2 and choice1 == 1:
        print ('Player two is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
        
    elif choice2 == 3 and choice1 == 2:
        print ('Player two is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
            
    elif choice2 == 3 and choice1 == 1:
        print('Player one is victorious!!!')
        play_again = input('Would you like to Battle again?\n y or n? ')
    if play_again == 'y':
        continue
    
    if play_again == 'n':
        break
    if play_again != 'y' or 'n':
        print ('Try again!')
        continue
    
