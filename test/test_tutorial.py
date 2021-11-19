import unittest
from src.tutorial import Tutorial

class TestTutorial(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(1, Tutorial.fizzbuzz(1))

