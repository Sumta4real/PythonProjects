# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:12:38 2021

@author: user
"""

from math import pi

def circle_area(r):
    if type(r) not in [float, int]:
        raise TypeError('The radius must be a non-negative real number')
    if r < 0:
        raise ValueError('The radius cannot be negative')
    return pi*(r**2)

#Test Function

#radii = [2,0,2.5,3+5j,True, 'radius']
#message = 'Area of circles with r = {radius} is {area}'

#for r in radii:
#    A = circle_area(r)
#    print(message.format(radius=r, area=A ))
    