'''Create the parent class'Figure' with the init method to initalize the color, get color 
- to return the color, gives info on the figure and color. Daughter classes: 'Rectangle' and 'Square'
that have info on width, height, and the square method to calculate the area'''
class Figure ():
    def __init__(self,color):
        self.color=color
    def get_color(self):
        print('The color of the figure is', self.color)

class Rectangle (Figure):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def square(self):
        print('The square of the rectangle is', self.width*self.height)   

class Square (Figure):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def square(self):
        print('The square of the square is', self.width*self.height)

f=Figure('yellow')
f.get_color()

r=Rectangle(3,4)
r.square()

s=Square(5,5)
s.square()