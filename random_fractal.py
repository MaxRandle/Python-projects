import turtle
def fractal(number_of_iterations):
    string = "0"
    while number_of_iterations > 0:
        string = iterate(string)
        number_of_iterations -= 1
    draw(string)

def iterate(string):
    new_string = ""
    for n in string:
        if n == "0":
            new_string += "1"
        else:
            new_string += "0"
            
    #regular dragon curve
    return string + "0" + new_string[::-1]

    #wiggly dragon curve
    #return (string + "0" + new_string[::-1])[1::]

    #maze dragon curve
    #return (string + "010" + new_string[::-1])[0:-1:]

    #maze triangle
    #return (string + "010" + new_string[::-1])[::-1][0:-1:]

    #weird square dragon curve
    #return string + "010" + new_string[::-1]

    #spiky dragon curve
    #return string + "1" + new_string[::-1]

    #crazy triangle
    #return string[::-1] + "010" + new_string
    
def draw(string):
    """uses turtle to draw the curve"""
    t = turtle.Turtle()
    t.speed(0)
    t.shape("blank")
    for n in string:
        if n == "0":
            t.right(90)
        elif n == "1":
            t.left(90)
        t.forward(4)

"""



    #wiggly dragon curve
    return (string + "0" + new_string[::-1])[1::]

    #maze dragon curve
    (string + "010" + new_string[::-1])[0:-1:]

    #maze triangle
    return (string + "010" + new_string[::-1])[::-1][0:-1:]

    #weird square dragon curve
    return string + "010" + new_string[::-1]

    #spiky dragon curve
    return string + "1" + new_string[::-1]

    #crazy triangle
    return string[::-1] + "010" + new_string
"""
