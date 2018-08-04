import random
import string

def p_gen():

    command = input ('Would you like me to generate a password? y or n: ')
    N = int(input ('How many digits do you want it to be? '))
    
    if command == 'y':
        password = ''
        password = password.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits \
                                                              + string.ascii_lowercase) for _ in range(N))
        print (password)  
                                 
    else:
        pass


p_gen()
    
