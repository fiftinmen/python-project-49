import random
from math import gcd


GAME_PROMPT = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def generate_pair_of_numbers():
    return [random.randint(1, MAX_NUMBER) for _ in range(2)]


def question_answer_generator():
    question = generate_pair_of_numbers()
    answer = gcd(*question)
    return ' '.join(map(str, question)), answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
