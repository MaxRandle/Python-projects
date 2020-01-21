import math
def projectile(angle, velocity, starting_height):
    """
    This function determines:
    the maximum height reached by the projectile (in metres)
    the range of the projectile (in metres)
    and the time taken for the projectile to land (in seconds)
    Arguments:
    angle - the angle in relation to the horizontal that the projectile
    was fired at (measured in degrees)
    velocity - the speed at which the projectile was launched
    starting_height - how high off the ground the projectile was fired from
    Returns:
    height - the aximum height above the ground reached by the projectile
    range - how far away the projectile lands
    time - how long the projectile is in the air for

    (note this function does not account for air resistance
    or weakening of the gravitational force due to distance from the
    earth increasing. This function assumes acceleration due to gravity is
    9.81m/s^2 and that the gound is flat.)
    """
    #V^2 = U^2 + 2 * a * s
    #s = U * t + 1/2 * a * t^2 
    g = 9.81
    
    #components of velocity
    verticle_velocity = velocity * math.sin(angle * math.pi / 180)
    print("verticle_velocity =", verticle_velocity)
          
    horizontal_velocity = velocity * math.cos(angle * math.pi / 180)
    print("horizontal_velocity =", horizontal_velocity)

    #maximum height (from ground)
    h_max = (verticle_velocity ** 2 / (2 * g)) + starting_height
    print("h_max =", h_max)
    
    #time taken to reach maximum height
    t_max = verticle_velocity / g
    print("t_max =", t_max)
    
    #time taken to land
    t_land = (h_max / 0.5 * g) ** 0.5 + t_max
    print("t_land =", t_land)
    
    #range
    range = horizontal_velocity * t_land
    print("range =", range)
    
import doctest
doctest.testmod()
