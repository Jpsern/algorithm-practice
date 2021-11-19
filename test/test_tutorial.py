import unittest
from src.tutorial import Tutorial

class TestTutorial(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual('Fizz', Tutorial.fizzbuzz(1))

