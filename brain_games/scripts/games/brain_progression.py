#!/usr/bin/env python3


import random
from . import brain_engine
from . import functions


def generate_progression():
    progression = ''
    progression_length = random.randint(0, 4)+5
    missing_element = random.randint(1, progression_length-1)
    number = random.randint(0, 50)
    progression_step = random.randint(1, 30)
    for i in range(0, progression_length):
        if i != missing_element:
            progression += f'{str(number)}, '
        else:
            progression += '..., '            
        number += progression_step
    progression += str(number)
    return progression


def find_missing_element(sequence: str) -> int:
    for i, el in enumerate(sequence):
        if el =='...':
            return i


def calc_missing_element(progression: str) -> int:
    elements = [n for n in progression.split(', ')]
    missing_element_index = find_missing_element(elements)
    return (int(elements[missing_element_index-1]) + int(elements[missing_element_index + 1])) // 2


rules = 'What number is missing in the progression?'


def main():
    brain_engine.game(rules=rules,
                      input_function=functions.integer_input,
                      question_generator=generate_progression,
                      correct_answer_generator=calc_missing_element)


if __name__ == '__main__':
    main()
