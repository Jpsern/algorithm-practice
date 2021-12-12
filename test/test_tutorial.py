import unittest
from src.tutorial import Tutorial

class TestTutorial(unittest.TestCase):
    def test_fizzbuzz_normal(self):
        for num in [1, 2, 4, 7, 8, 11, 13, 14, 16]:
            self.assertEqual(Tutorial.fizzbuzz(num), num, '渡した値をそのまま返す')

    def test_fizzbuzz_multiple_three(self):
        for num in [3, 6, 9, 12]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'Fizz', '3の倍数はFizzを返す')

    def test_fizzbuzz_multiple_five(self):
        for num in [5, 10, 20, 25]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'Buzz', '5の倍数はBuzzを返す')

    def test_fizzbuzz_multiple_fifteen(self):
        for num in [15, 30, 45, 60]:
            self.assertEqual(Tutorial.fizzbuzz(num), 'FizzBuzz', '15の倍数はFizzBuzzを返す')
    
    def test_is_prime_number(self):
        self.assertListEqual(
            list(filter(
                lambda x: Tutorial.is_prime_number(x), range(1, 20)
            )),
            [2, 3, 5, 7, 11, 13, 17, 19],
            '素数だけが配列に格納される'
        )

    def test_convert_to_binary_number(self):
        self.assertEqual(Tutorial.convert_to_binary_number(18), 10010, '10進数を2進数に変換する')

    def test_convert_to_decimal_number(self):
        self.assertEqual(Tutorial.convert_to_decimal_number(10010), 18, '2進数を10進数に変換する')
