import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_classe(self):
        classe = FileStorage()
        self.assertEqual(classe.reload(), {})

