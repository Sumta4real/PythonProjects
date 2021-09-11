# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:28:49 2021

@author: user
"""

import unittest

from circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >= 0 
        #check if the function correctly computes the area of the circles
        self.assertAlmostEqual(circle_area(0), 0) #checks if first and second value are equal
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.9), pi* (2.9**2))
        
    def test_values(self):
        #Make sure vaues error are raised when neccessary
        self.assertRaises(ValueError, circle_area, -2)
        
    def test_type(self):
        #make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 2+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 'radius')