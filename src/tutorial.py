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

    def is_prime_number(cls, num: int):
        if num <= 1:
            return False
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                return False
        return True

