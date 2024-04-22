import random

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
VAR_PROGRESSION_LENGTH = MAX_PROGRESSION_LENGTH - MIN_PROGRESSION_LENGTH

HIDDEN_ELEMENT_MARKER = '..'

MAX_START_NUMBER = 50
MAX_PROGRESSION_STEP = 30

GAME_PROMPT = 'What number is missing in the progression?'


def generate_progression():
    progression = []
    progression_length = random.randint(0, VAR_PROGRESSION_LENGTH) + \
        MIN_PROGRESSION_LENGTH
    missing_element_range = (1, progression_length - 2)
    missing_element = random.randint(*missing_element_range)
    number = random.randint(0, MAX_START_NUMBER)
    progression_step = random.randint(1, MAX_PROGRESSION_STEP)
    for _ in range(progression_length):
        progression.append(number)
        number += progression_step

    progression[missing_element] = HIDDEN_ELEMENT_MARKER
    question = ', '.join(map(str, progression))
    return progression, question


def find_missing_element(sequence: str) -> int:
    for i, el in enumerate(sequence):
        if el == HIDDEN_ELEMENT_MARKER:
            return i


def calc_missing_element(progression: list) -> int:
    missing_element_index = progression.index(HIDDEN_ELEMENT_MARKER)
    return (progression[missing_element_index - 1]
            + progression[missing_element_index + 1]) // 2


def question_answer_generator():
    progression, question = generate_progression()
    answer = calc_missing_element(progression)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
