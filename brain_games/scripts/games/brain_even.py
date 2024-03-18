#!/usr/bin/env python3

from . import brain_engine
from . import functions


def even_yes_or_no(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.yes_no_input,
                      question_generator=functions.generate_number,
                      correct_answer_generator=even_yes_or_no)


if __name__ == '__main__':
    main()
