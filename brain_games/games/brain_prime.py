from math import sqrt
import random


GAME_PROMPT = 'Answer "yes" if given number is prime. '\
    'Otherwise answer "no".'
MAX_NUMBER = 100


def prime_yes_no(number: int) -> str:
    if number < 4:
        return 'yes'
    first_prime = 2
    max_possible_divisor = int(sqrt(number))
    not_prime = all(
        number % i != 0 for i in range(first_prime, max_possible_divisor + 1)
    )
    return 'yes' if not_prime else 'no'


def question_answer_generator():
    question = random.randint(2, MAX_NUMBER)
    answer = prime_yes_no(question)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
