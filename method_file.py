import math

class Square:
    def __init__(self, length):
        self.size = length
        
    def perimeter(self):
        return self.size*4

    def scale(self, factor):
        return Square(self.size*factor)

    def is_bigger(self, other):
        return self.area() > other

    def area(self):
        return self.size**2

    def __repr__(self):
        return 'Square({})'.format(self.size)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
        
    def area(self):
        return self.width * self.height 
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __ge__(self, other):
        return self.area() >= other.area()
        
    def __eq__(self, other):
        return self.area() == other.area()
        
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    
class Fraction:
    def __init__(self, top, bottom):
        self.num = top      #numerator
        self.den = bottom   #denominator
        
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    def __repr__(self):
        return '{}/{}'.format(self.num, self.den)
    
class Point:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y

    def modulus(self):
        return (self.x**2 + self.y**2)**0.5

    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)

class Quadratic:
    def __init__(self, a, b, c):
        self.eqn = (a, b, c)
        self.a = a
        self.b = b
        self.c = c
        self.s = self.solve()

    def __repr__(self):
        return "y = {}x^2 + {}x + {}".format(self.a, self.b, self.c)

    def solve(self):
        x1 = (-self.b + (self.b**2 - 4 * self.a * self.c)**0.5)/(2 * self.a)
        x2 = (-self.b - (self.b**2 - 4 * self.a * self.c)**0.5)/(2 * self.a)
        return "x = {}, x = {}".format(x1, x2)

    def grad_function(self):
        return 'dy/dx = {}x + {}'.format(self.a * 2, self.b)

    def grad(self, a):
        return self.a * 2 * x + self.b

    def integrate(self):
        return "{}x^3 + {}x^2 + {}x + k".format(self.a/3, self.b/2, self.c)

    def definite_integral(self, x1, x2):
        bound1 = x1*(self.a/3)**3 + x1*(self.b/2)**2 + x1*self.c
        bound2 = x2*(self.a/3)**3 + x2*(self.b/2)**2 + x2*self.c
        return abs(bound1-bound2)

    def factorise(self):
        pass

    




    
