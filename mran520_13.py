"""Calculates the distance between two points on the Earth.

Requires the latitude and longitude of those points.

Name: Maxwell Randle
UPI: mran520
ID: 9607474
"""

import math

earth_radius = 6371

#My house: -36.870592,174.743621
lat1 = math.radians(-36.870592)
long1 = math.radians(174.743621)

#clock tower (36 princes street) -36.850202,174.769558
lat2 = math.radians(-36.850202)
long2 = math.radians(174.769558)

distance = 2 * earth_radius * math.asin(math.sqrt(
    math.sin((lat2 - lat1) / 2) ** 2 + 
    math.cos(lat1) * math.cos(lat2) * 
    math.sin((long2 - long1) / 2) **2))

print(distance)
