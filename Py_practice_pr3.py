#list less than ten


x = []
x.append(3)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34,55, 89]
b = []



for x in a:
    if x < 5:
        print (x)
        b.append (x)
print (b)

c = int(input('Enter a number: '))

d = []

for x in a:
    if x < c:
        d.append (x)
print (d)


