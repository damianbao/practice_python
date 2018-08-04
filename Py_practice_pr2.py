#print out message if number is even or odd.

num = int(input('Enter a number: '))
check = int(input('Enter a number to divide by: '))

num = num/check



if num % 2 == 0:
    print('This number is even.')

if num % 4 == 0:
    print('It is also divisible by 4.')
    
else:
    print('This number is odd.')
