#!/usr/bin/python3
'''test module unittest for file amenity.py'''

import unittest
from models.amenity import Amenity

class Test_Amenity(unittest.TestCase):
    '''class Test'''
    def test_Name(self):
        ame = Amenity(name="sauna")
        self.assertEqual(ame.name, "sauna")