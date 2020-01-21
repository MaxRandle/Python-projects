import math

def celcius_to_farrenheight(c):
        f = (9/5)*(c+32)
        return f
        """
        This function converts temperatures from celcius to farrenheight
        arguents: c - temperature in degrees celcius (float)
        returns: f - temperature in degrees farrenheight (float)
        

    """

def farrenheight_to_celcius(f):
    c = (5/9)*(f-32)
    return c

def area_of_triangle(base, height):
    """
    calculates the area of a triangle using given values for base and height.
    arguments:
    Height - height of the triagnle
    Base - width of triangle across its base
    Returns:
    area of triangle (float)
    
    >>>area_of_triangle(10, 10):
    50.0
    
    """
    area_of_triangle = 0.5 * base * height
    return area_of_triangle

def kg_to_pounds(kg):
    """
    Converts from Kilograms to pounds:

    Arguents:
        kg - number of kilograms (float)

    Returns:
        mass in pounds (float)
    """
    pounds = kg * 2.2
    return pounds

def miles_to_km(miles):
    """converts from miles to kilometers

    Arguments:
        miles - number of miles (float)

    Returns:
        number of kilometers (float)
    """

    km = miles * 1.60934
    return km

def kg_to_pounds(kg):
    """
    Converts from Kilograms to pounds:

    Arguents:
        kg - number of kilograms (float)

    Returns:
        mass in pounds (float)
    """
    pounds = kg * 2.2
    return pounds

def kmph_to_mps(kmph):
    mps = (kmph/3.6)
    return mps

def mps_to_kmph(mps):
    kmph = mps*3.6
    return kmph

def circle_area(radius):
        """
        calculates the area of a circle
        arguments:
        radius - the radius of the circle
        returns:
        the area (float)
        >>>circle_area(0)
        0
        >>>circle_area(1)
        3.14159265
        """
        return math.pi * radius ** 2

def annulus(outer, inner):
        """
        calculates the area of an annulus

        Arguments:
            outer -  the radius of the exterior
            inner - the radius of the interior

        Returns:
            the area of the annulus

        >>>annulus(1.0, 1.0)
        0.0
        >>>round (annulus(1.0, 0.0), 8)
        3.14159265
        """
        area = circle_area(outer) - circle_area(inner)
        return area

def tube_volume(outer, inner, length):
        """
        calculates the volume of a tube

        Arguments:
        inner - the radius of the inside surface
        outer - the radius of the outside surface
        length - the length of the tube

        Returns:
        the volume of the tube

        >>> tube_volume(1, 1, 34)
        0.0
        >>> round (tube volume(1, 0, 10), 7)
        31.4159265
        """
        return annulus(outer, inner) * length

def weight_tube(outer, inner, length):
        """
        calculates the weight of a steel tube.

        Arguents:
            outer - the radius of the exterior surface (in centermetres)
            inner - the radius of the interior radius (in centermetres)
            length - the length of the tube (in centermetres)
        Returns:
            the weight of the tube (in grams)
        """
        steel_density = 7.85 #grams per centimetre
        weight = tube_volume(outer, inner, length) * steel_density
        return weight

def RTTtau(km, RTT):
        km = (2000*km)/(3*10**8)
        return (RTT/1000) / km

import doctest
doctest.testmod()
