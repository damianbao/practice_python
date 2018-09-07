#create a list represetnation of coyote population and manipulate data
import random

def print_grid ():
    for r in rows:
        for c in r:
            print ("{0:3s}".format (str(c)), end = '') #end at '' instead of starting on a new line. default is end ='\n'
        print() #empty print on a line
def update_cell (c_id, r, c):
    rows [r][c] = c_id
#capitalize global variables
#lowercase for variables isolated to a certain function
    
rows = []

coyotes = []

for _ in range (10): #saves computer cycles/ does for 10 times/ only use when you dont need it again
    cols = []
    for _ in range (12):
        cols.append('-')
        rows.append(cols)

    
print_grid()
print ()

for p in range (10):
    r = random.randint (0, 9)
    c = random.randint (0, 11)
    coyotes.append ([r, c])
    update_cell (p, r, c)
print_grid()


# dir = random.radint (1,5)
# 1=north
# 2=east
# 3=west
# 4=south
# 5= stays put

    if dir = 1:
        r=r+1
    
