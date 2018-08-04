#Create a program that asks the user for a number and
#then prints out a list of all the divisors of that number.


num = int(input('Enter a number: '))

x = range(1,num + 1)

divisors = []


for elem in x:
    if num % elem == 0:
        divisors.append (elem)

print ('Divisors = ' + str(divisors))
