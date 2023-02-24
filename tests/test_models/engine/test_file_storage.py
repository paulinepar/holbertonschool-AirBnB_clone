import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_path(self):
        self.assertEqual(FileStorage.__file_path, "")
        
    def test_object(self):
        self.assertEqual(FileStorage.__objects, "{}")
     
    def test_all(self):
        classe = FileStorage()
        self.assertEqual(classe.all(), "{}")   