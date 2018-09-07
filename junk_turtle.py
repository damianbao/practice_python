
from turtle import *
from random import choice



def square (length):
    t.pd()
    for s in range(4):
        t.fd(100)
        t.lt(90)
    t.pu()
    
t = Turtle()
colors =['green', 'blue', 'red', 'orange','pink','cyan']
bgcolor ('grey')

t.shape('turtle')

t.pencolor('red')

t.fillcolor('purple')



for _ in range (24):
    t.begin_fill()
    t.color(choice(colors))
    square(100)
    t.lt(15)
    t.end_fill()
    



    