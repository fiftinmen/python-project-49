#!/usr/bin/env python3


import prompt
import random
from . import brain_engine
from . import functions


def generate_expression():
    operations = {
        1: '+',
        2: '-',
        3: '*',
        4: '/'
    }
    numbers_list = [functions.generate_number() for _ in range(2)]
    operation = operations[random.randint(1, 4)]
    return f'{numbers_list[0]} {operation} {numbers_list[1]}'


def evaluate_expression(expression: str) -> int:
    return round(eval(expression))


def brain_calc_input():
    return prompt.integer(prompt='Your answer: ', empty=False)


rules = 'What is a result of expression?' + \
    '(In case of division round to the nearest integer number)'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.integer_input,
                      question_generator=generate_expression,
                      correct_answer_generator=evaluate_expression)


if __name__ == '__main__':
    main()
