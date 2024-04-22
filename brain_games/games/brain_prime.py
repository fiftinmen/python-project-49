from math import sqrt
import random


GAME_PROMPT = 'Answer "yes" if given number is prime. '\
    'Otherwise answer "no".'
MAX_NUMBER = 100
FIRST_NOT_PRIME = 4
FIRST_PRIME = 2


def is_prime(number: int) -> str:
    if number < FIRST_NOT_PRIME:
        return 'yes'
    max_possible_divisor = int(sqrt(number))
    return all(
        number % i != 0 for i in range(FIRST_PRIME, max_possible_divisor + 1))


def question_answer_generator():
    question = random.randint(0, MAX_NUMBER)
    answer = is_prime(question)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
