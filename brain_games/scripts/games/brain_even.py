#!/usr/bin/env python3


import prompt
import random
from . import brain_engine


def generate_number():
    return random.randint(-1000, 1000)


def even_yes_or_no(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def brain_even_input():
    pattern = r'(yes)|(no)'
    answer = prompt.regex(pattern, prompt='Your answer: ', empty=False)
    answer = answer.groups()
    # получили массив из двух элементов:
    # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
    return answer[0] if answer[0] else answer[1]


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    brain_engine.game(rules=rules,
                      input_function=brain_even_input,
                      question_generator=generate_number,
                      correct_answer_generator=even_yes_or_no)


if __name__ == '__main__':
    main()
