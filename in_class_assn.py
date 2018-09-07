

def ascend (a,b):
    concat = a + b
    if a>b:
        return [a,b], concat
    else:
        return [b,a], concat
x,y = ascend (9,0)


x = 123
def fun (a):
    x = -123 *3
    return x
x = fun (3)


import time

print (x) 
y = time.ctime()


f= open('in_class_assn.txt','w')
f.write(str(x))

f.write('date:')
f.write(y)
f.close()

print (f)


      

      
      
      
