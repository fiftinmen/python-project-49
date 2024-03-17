#!/usr/bin/env python3


import random
from . import brain_engine
from . import functions


def generate_pair_of_numbers():
    return str(random.randint(1, 100))+' '+str(random.randint(1, 100))


def calc_greatest_common_divisor(pair_of_numbers: str) -> int:
    numbers = [int(n) for n in pair_of_numbers.split(' ')]
    while numbers[0] != numbers[1]:
        if numbers[0] > numbers[1]:
            numbers[0] = numbers[0] - numbers[1]
        else:
            numbers[1] = numbers[1] - numbers[0]
    return numbers[0]



rules = 'Find the greatest common divisor of given numbers.'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.integer_input,
                      question_generator=generate_pair_of_numbers,
                      correct_answer_generator=find_greatest_common_divisor)


if __name__ == '__main__':
    main()
