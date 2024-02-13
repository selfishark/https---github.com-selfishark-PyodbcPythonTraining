# tests/test_multireader.py

import unittest

# test directory is not part of the package hence the import (no relative path)
import src.demo_reader.multireader

class TestMultireader(unittest.TestCase):
    def test_initialisation(self):
        src.demo_reader.multireader.MultiReader('test_file.txt')
