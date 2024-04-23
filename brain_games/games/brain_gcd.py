import random
from math import gcd


GAME_PROMPT = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100
MIN_NATURAL_NUMBER = 1
LENGTH_OF_PAIR = 2


def generate_pair_of_numbers():
    return [random.randint(MIN_NATURAL_NUMBER, MAX_NUMBER)
            for _ in range(LENGTH_OF_PAIR)]


def generate_question_and_answer():
    question = generate_pair_of_numbers()
    answer = str(gcd(*question))
    return ' '.join(map(str, question)), answer


__all__ = {
    'GAME_PROMPT',
    'generate_question_and_answer',
}
