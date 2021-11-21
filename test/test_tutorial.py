import unittest
from src.tutorial import Tutorial

class TestTutorial(unittest.TestCase):
    def test_fizzbuzz_normal(self):
        for num in [1, 2, 4, 7, 8, 11, 13, 14, 16]:
            self.assertEqual(Tutorial.fizzbuzz(num), num, '渡した値をそのまま返す')

    def test_fizzbuzz_multiple_three(self):
        for num in [3, 6, 9, 12]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'Fizz', 'Fizzを返すべき')

    def test_fizzbuzz_multiple_five(self):
        for num in [5, 10, 20, 25]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'Buzz', 'Buzzを返すべき')

    def test_fizzbuzz_multiple_fifteen(self):
        for num in [15, 30, 45, 60]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'FizzBuzz', 'FizzBuzzを返すべき')
    
    def test_is_prime_number(self):
        # とりあえず適当
        self.assertTrue(Tutorial.is_prime_number(7))
        self.assertFalse(Tutorial.is_prime_number(8))
