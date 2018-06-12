import unittest

from main import myabs


class TestAbs(unittest.TestCase):
    def test__positive(self):
        self.assertEqual(myabs(4),4)
        
    def test__negative(self):
        self.assertEqual(myabs(-4),4)