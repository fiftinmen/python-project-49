from math import sqrt
import random


GAME_PROMPT = 'Answer "yes" if given number is prime. '\
    'Otherwise answer "no".'
MAX_NUMBER = 100
FIRST_PRIME = 2
FIRST_NATURAL_NUMBER = 1


def is_prime(number: int) -> str:
    if number < FIRST_PRIME:
        return False
    max_possible_divisor = int(sqrt(number))
    if max_possible_divisor < FIRST_PRIME:
        return True
    return all(
        number % i != 0
        for i in range(FIRST_PRIME, max_possible_divisor + 1)
        )


def generate_question_and_answer():
    question = random.randint(FIRST_NATURAL_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'generate_question_and_answer',
}
