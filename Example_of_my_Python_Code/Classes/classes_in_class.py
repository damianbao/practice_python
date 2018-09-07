#print (Square.__doc__) prints the entire code of the class?

#class Square(object): #means square is pulling from the most
#   generic class of that that type
import math 
import turtle as t
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()

class Square:  #(object is assumed
    """This is a square class."""
    count = 0
    def __init__(self, bw, bc, fc, length, loc, bt):  # self is a required parameter
        self.border_width = bw
        self.border_color = bc
        self.fill_color = fc
        self.length = length
        self.loc = loc
        self.border_type = bt
        Square.count += 1
        self.id = Square.count
        

    def area(self):
        return self.length * self.length
    def perimeter(self):
        return self.length *4
    def draw(self, t):
        t.pu()
        t.setpos (self.loc)
        t.color (self.border_color, self.fill_color)
        t.pd()
        t.begin_fill()
        for _ in range(4):
            t.fd (self.length)
            t.lt (90)
        t.end_fill()
        t.pu()

class Triangle:
    def __init__(self, bw, bc, fc, a, b, c, loc, bt):
        self.border_width = bw
        self.border_color = bc
        self.fill_color = fc
        self.a = a
        self.b = b
        self.c = c
        self.s = (a+b+c)/2
"""     self.angle_a = int(math.degrees(math.acos((b**2+c**2-a**2)/2*b*c)))
        self.angle_b = math.degrees(math.acos((a**2+c**2-b**2)/2*a*c))
        self.angle_c = math.degrees(math.acos((a**2+b**2-c**2)/2*a*b))
"""     self.loc = loc
        self.border_type = bt
        Triangle.count += 1
        self.id = Triangle.count

        #def area(self):
           # return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**(1/2)
        #def perimeter(self):
           # return self.a+self.b+self.c

        
tri1 = Triangle(8, 'blue', 'purple', 4, 5, 6, (0,0), 'dashed') 
        
"""        def draw(self, t):
            t.pu()
            t.setpos (self.loc)
            t.color (self.border_color, self.fill_color)
            t.pd()
            t.begin_fill()
            for _ in range(4):
                t.fd (self.length)
                t.lt (90)
            t.end_fill()
            t.pu()
"""
    
    
sq1 = Square(3, 'red', 'blue', 30, (100, 100), 'dashed')
# always one less parameter than in the class init
sq2 = Square(5, 'yellow', 'orange', 50, (-100, -100), 'dashed')
sq3 = Square(2, 'yellow', 'pink', 150, (-175, 100), 'dashed')
print (sq1.area(), sq2.area(), sq3.area())
print (tri1)

sq1.draw(t1)
sq2.draw(t2)
sq3.draw(t3)
