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
    return progression


def calc_missing_element(progression: list) -> int:
    missing_element_index = progression.index(HIDDEN_ELEMENT_MARKER)
    return (progression[missing_element_index - 1]
            + progression[missing_element_index + 1]) // 2


def generate_question_and_answer():
    progression = generate_progression()
    question = ' '.join(map(str, progression))
    answer = str(calc_missing_element(progression))
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'generate_question_and_answer',
}
