import unittest
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    def test_classe(self):
        classe = FileStorage()
        self.assertEqual(classe.reload(), {})

    def test_all(self):
        classe = FileStorage()
        self.assertNotEqual(classe.all(), "{}")