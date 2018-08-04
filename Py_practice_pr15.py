def flip_it():
    phrase = input('Please enter your favorite phrase.\n')
    flip = phrase.split()
    it =('Reverse it:')
    for i in reversed(flip):
        it = it + ' ' + i
    print (it)

flip_it()
