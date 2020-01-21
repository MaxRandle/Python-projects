import turtle
def Bevans_mum(itterations):
    xstring = "0"
    while itterations > 0:
        xstring = itterate(xstring)
        itterations -= 1
    draw(xstring)

def itterate(xstring):
    new_string = ""
    for n in xstring[::-1]:
        if n == "0":
            new_string += "1"
        else:
            new_string += "0"
    return xstring + "0" + new_string

def draw(xstring):
    t = turtle.Turtle()
    t.speed(0)
    #t.shape(0)
    for n in xstring:
        if n == "0":
            t.right(90)
        elif n == "1":
            t.left(90)
        t.forward(8)
    

