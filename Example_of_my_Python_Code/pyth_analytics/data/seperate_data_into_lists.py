import os
import numpy as np

def read_day_data (f):
    day_data =[]
    while True:
        line = f.readline()

        if line:
            print (line)
            line_split = line.split()
            print (line_split)
            day_data.append (line_split)
        else:
            break

    return (day_data)   



def collect_day_data ():
    days = []
    for f in os.listdir():
        print (f)
        if f[-4:] == '.txt':
             f1 = open (f, 'r')
             day = read_day_data (f1)
             days.append (day)
             f1.close ()
    return days



all_the_data = collect_day_data ()
"""
for d in all_the_data:
    for h in d:
        days.append(h)
        print ()    
print ()
"""
print (all_the_data)
for f in os
f1 = open (f, 'r')
read_day_data ()

temp_avg = []

t = 600
for d in all_the_data:
    for h in d:
        if int(h[0]) == t:
            x=12
            y=0
            y = y +int(h[2])
        z=0
        z=round(y/x,2)
        print(t,z,x,y)
        temp_avg.append(z)
            
    t += 100
    if t == 2400:
        t = 0000        
print (temp_avg)      
            