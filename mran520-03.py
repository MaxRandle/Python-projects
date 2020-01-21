"""
Maxwell Randle
mran520
9607474
"""
import math

def cone_volume(bottom_radius, top_radius, height):
    """calculates the volume of a trunkated  cone.
    Arguments:
        bottom_radius - the radius of the bottom cirlce in cm (float)
        top_radius - the radius of the top cirlce in cm (float)
        height - how tall the cone is in cm (float)

    Returns:
        the volume of the cone in cm^3 (float)

    Test cases:
    >>> cone_volume(2, 3, 10)
    198.97
    >>> cone_volume(4, 10, 5)
    816.81
    >>> cone_volume(1, 8, 2)
    152.89
    """
    volume = (math.pi / 3) * height * \
    (bottom_radius**2 + top_radius*bottom_radius + top_radius**2)
    
    return round(volume, 2)

def number_of_cups(bottom_radius, top_radius, height, litres):
    """calculates the number of cups needed to hold a given quantity of liquid
    Arguments:
        bottom_radius - the radius of the bottom cirlce in cm (float)
        top_radius - the radius of the top cirlce in cm (float)
        height - how tall the cone is in cm (float)
        litres - the ammount of liquid in litres (float)
        
    Returns:
        number - the maximum number of cups that can be completely filled (int)

    test cases
    >>> number_of_cups(1, 2, 3, 4)
    181
    >>> number_of_cups(4, 7, 3.5, 10)
    29
    >>> number_of_cups(6, 8, 9, 5)
    3
    """
    volume = (math.pi / 3) * height * \
    (bottom_radius**2 + top_radius*bottom_radius + top_radius**2)

    number = (litres * 1000) / volume
    return math.floor(number)

import doctest
doctest.testmod()
