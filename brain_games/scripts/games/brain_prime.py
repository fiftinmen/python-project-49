#!/usr/bin/env python3

from .. import brain_engine
from .. import functions


def prime_yes_or_no(number: int) -> str:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.yes_no_input,
                      question_generator=functions.generate_natural_number,
                      correct_answer_generator=prime_yes_or_no)


if __name__ == '__main__':
    main()
