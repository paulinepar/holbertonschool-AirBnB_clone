import unittest
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    
    
    def test_class(self):
        classe = BaseModel()
        classe.id = str(uuid.uuid4())
        self.assertEqual(str, type(classe.id))
        
    def test_update(self):
        classe = BaseModel()
        classe.update({"name": "bonjour"})
        self.assertEqual(classe.name, "bonjour")
        
    def test_init(self):
        obj = {"checker": "OK"}
        classe = BaseModel(**obj)
        self.assertEqual(classe.checker, "OK")
        
    
