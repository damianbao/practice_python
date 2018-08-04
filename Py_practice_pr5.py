import random as r

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new = []
 
for x in b:
    if x in a:
        new.append (x)

print (new)
        
[new.append (x) for x in b if x in a]

print (new)


c = [r.randrange(0,50,1) for i in range(0,50,1)]
d = [r.randrange(0,50,1) for i in range(0,50,1)]

print (c, '\n', d)

e = r.sample(range(100), 5)
print ('C: \n%s' %c)
f = r.sample(range (100),5)
print ('D: \n%s' %d)

def list_overlap(a,b):
    new_lst = []
    for item in b:
        if item in a and item not in new_lst:
            new_lst.append(item)
            return new_lst
        
print (list_overlap (c,d))
print (list_overlap (e,f))