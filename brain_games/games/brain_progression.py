import random
from brain_games.common_functions import integer_input

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
VAR_PROGRESSION_LENGTH = MAX_PROGRESSION_LENGTH - MIN_PROGRESSION_LENGTH

HIDDEN_ELEMENT_MARKER = '..'

MAX_START_NUMBER = 50
MAX_PROGRESSION_STEP = 30


BRAIN_PROGRESSION_PROMPT = 'What number is missing in the progression?'


def generate_progression():
    progression = []
    progression_length = random.randint(0, VAR_PROGRESSION_LENGTH) + \
        MIN_PROGRESSION_LENGTH
    missing_element_range = (1, progression_length - 2)
    missing_element = random.randint(*missing_element_range)
    number = random.randint(0, MAX_START_NUMBER)
    progression_step = random.randint(1, MAX_PROGRESSION_STEP)
    for i in range(0, progression_length):
        progression.append(str(number))
        number += progression_step

    progression[missing_element] = HIDDEN_ELEMENT_MARKER
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


game_prompt = BRAIN_PROGRESSION_PROMPT
question_generator = generate_progression
input_function = integer_input
correct_answer_generator = calc_missing_element

__all__ = {
    'game_prompt',
    'question_generator',
    'input_function',
    'correct_answer_generator'
}
