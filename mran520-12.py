"""
calculates the BMI (body-mass index)
requires height and weight

Name: Maxwell Randle
UPI: mran520
ID: 9607474
"""

def BMI(height, weight):
    """
    calculates BMI
    Arguments:
        height - how tall the person is in metres
        weight - how much the person weighs (Kg)
    Returns:
        BMI - the body-mass index (kg/m^2)
    """
    BMI = weight / height**2
    return BMI
