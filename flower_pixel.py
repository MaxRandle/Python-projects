#from ImageLibrary import*
"""gets pixel averages of RGB then finds a flower closest to these values and substitutes it in"""
import random

def get_flowers():
    flower_number = ""
    flower_list = []
    for number in range(1,501,1):
        if number < 10:
            flower_number = "00" + str(number)
        elif number < 100:
            flower_number = "0" + str(number)
        elif number < 1000:
            flower_number = str(number)
        flower_file = "{}.png".format(flower_number)
        flower_list += [flower_file]
    return flower_list


def get_grid(width, height):
    cols = width//8
    rows = height//6
    grid = []
    print(cols, rows)
    for y in range(0, rows):
        for x in range(0, cols):
            cell = (x,y)
            grid += [cell]
    return grid

def showpic(file):
    image = makePicture(file)
    show(image)
    print(image)
    pixel = getPixel(image, 100, 25)

def get_pixels(cell, x, y):
    pixel_list = []
    coord_x, coord_y = cell
    for cell_y in range(coord_y * y, coord_y*y +y):
        for cell_x in range(coord_x * x, coord_x * x + x):
            pixel_list += [(cell_x, cell_y)]
    return pixel_list

def get_RGB(image, pixel_tuple):
    x, y = pixel_tuple
    pixel = getPixel(image, x, y)

def position():
    x = random.randint(0, 960)
    y = random.randint(0, 1280)
    return (x, y)
