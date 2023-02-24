import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestCity(unittest.TestCase):
    def test_class(self):
        classe = City()
        
        