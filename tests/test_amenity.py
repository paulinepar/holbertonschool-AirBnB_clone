#!/usr/bin/python3
'''test module unittest for file amenity.py'''

import unittest
from models.amenity import Amenity

class Test_Amenity(unittest.TestCase):
    '''class Test'''
    def test_Name(self):
        '''test if is right name'''
        ame = Amenity(name="sauna")
        self.assertEqual(ame.name, "sauna")

    def test_str(self):
        '''test if is str'''
        self.assertEqual(str, type(Amenity.name))
