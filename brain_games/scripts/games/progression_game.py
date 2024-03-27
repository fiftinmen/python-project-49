import random
from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import integer_input

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


BRAIN_PROGRESSION_PROMPT = 'What number is missing in the progression?'


def brain_progression():
    game(
        game_prompt=BRAIN_PROGRESSION_PROMPT,
        input_function=integer_input,
        question_generator=generate_progression,
        correct_answer_generator=calc_missing_element
        )
