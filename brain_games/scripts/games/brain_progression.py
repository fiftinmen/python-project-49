#!/usr/bin/env python3


import random
from .. import brain_engine
from .. import functions


HIDDEN_ELEMENT_MARKER = '..'
MAX_PROGRESSION_STEP = 30
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
VAR_PROGRESSION_LENGTH = MAX_PROGRESSION_LENGTH - MIN_PROGRESSION_LENGTH
MAX_START_NUMBER = 50


def generate_progression():
    progression = []
    progression_length = random.randint(0, VAR_PROGRESSION_LENGTH) + \
        MIN_PROGRESSION_LENGTH
    missing_element = random.randint(1, progression_length - 2)
    number = random.randint(0, MAX_START_NUMBER)
    progression_step = random.randint(1, MAX_PROGRESSION_STEP)
    for i in range(0, progression_length):
        if i != missing_element:
            progression.append(str(number))
        else:
            progression.append(HIDDEN_ELEMENT_MARKER)
        number += progression_step
    return ' '.join(progression)


def find_missing_element(sequence: str) -> int:
    for i, el in enumerate(sequence):
        if el == HIDDEN_ELEMENT_MARKER:
            return i


def calc_missing_element(progression: str) -> int:
    elements = [n for n in progression.split(' ')]
    missing_element_index = find_missing_element(elements)
    return (int(elements[missing_element_index - 1])
            + int(elements[missing_element_index + 1])) // 2


rules = 'What number is missing in the progression?'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.integer_input,
                      question_generator=generate_progression,
                      correct_answer_generator=calc_missing_element)


if __name__ == '__main__':
    main()
