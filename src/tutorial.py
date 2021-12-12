import math

class Tutorial:
    @classmethod
    def fizzbuzz(cls, value: int):
        if value % 15 == 0:
            return 'FizzBuzz'
        if value % 5 == 0:
            return 'Buzz'
        if value % 3 == 0:
            return 'Fizz'
        else:
            return value

    @classmethod
    def is_prime_number(cls, num: int):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) +1):
            if num % i == 0:
                return False
        return True

    @classmethod
    def convert_to_binary_number(cls, num: int):
        result = ''
        while num > 0:
            result = str(num % 2) + result
            num //= 2
        return int(result)
