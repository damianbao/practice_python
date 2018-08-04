def am_i_prime ():
    num = int(input('Enter a number: '))
    
    x = range(1,num + 1)
    
    divisors = []
    
    [divisors.append(elem) for elem in x if num % elem == 0]
    
    print ('Divisors = ' + str(divisors))
    if len(divisors) == 2:
        print ("Your number is prime!")
        
am_i_prime(17)