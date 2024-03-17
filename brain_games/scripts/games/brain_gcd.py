#!/usr/bin/env python3


import prompt
import random
from . import brain_engine
from . import functions


def generate_pair_of_numbers():
    return str(random.randint(1, 100))+' '+str(random.randint(1, 100))


def find_greatest_common_divisor(pair_of_numbers: str) -> int:
    numbers = [int(n) for n in pair_of_numbers.split(' ')]
    upper_limit = min(numbers[0] // 2, numbers[1] // 2)
    for n in range(upper_limit, 0, -1):
        if numbers[0] % n == 0 and numbers[1] % n == 0:
            return n



rules = 'Find the greatest common divisor of given numbers.'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.integer_input,
                      question_generator=generate_pair_of_numbers,
                      correct_answer_generator=find_greatest_common_divisor)


if __name__ == '__main__':
    main()
