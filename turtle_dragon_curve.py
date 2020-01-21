import turtle
class Dragoncurve:
    def __init__(self, number_of_iterations, angle=90, starting_angle=0, size=4):
        """generates sequence which will be used to draw curve"""
        self.num = number_of_iterations
        self.ang = angle
        self.sta = starting_angle
        self.size = size
        self.seq = ""
        count = 0
        while count < self.num:
            self.seq += "0"
            self.seq += self.invert_sequence(self.seq[0:-1:])
            count += 1
        self.draw = self.draw_curve()

    def invert_sequence(self, sequence):
        """flips retrograde then inverts digits"""
        inverted_sequence = ""
        for n in sequence[::-1]:
            if n == "0":
                inverted_sequence += "1"
            elif n == "1":
                inverted_sequence += "0"
        return inverted_sequence
    
    def draw_curve(self):
        """uses turtle to draw the curve"""
        t = turtle.Turtle()
        t.speed(0)
        t.shape("blank")
        t.right(self.sta)
        for n in self.seq:
            if n == "0":
                t.right(self.ang)
            elif n == "1":
                t.left(self.ang)
            t.forward(self.size)

"""
0
001
0010011
001001100011011
"""


    
"""
x = t.position

#1st itteration
t.posision = x
x = t.position
t.forward(20)

#2nd itteration
t.right(90)
t.posision = x
x = t.position
t.forward(20)

#3rd itteration
t.right(90)
t.posision = x
x = t.position
t.forward(20)
t.right(90)
t.posision = x
x = t.position
t.forward(20)

"""
