from math import sqrt
from brain_games.common_functions import (bool_to_yes_no,
                                          yes_no_input,
                                          generate_natural_number
                                          )


BRAIN_PRIME_PROMPT = 'Answer "yes" if given number is prime. '\
    + 'Otherwise answer "no".'


def is_prime(number: int) -> str:
    if number in (0, 1):
        return None
    if number < 4:
        return True
    first_prime = 2
    max_possible_divisor = int(sqrt(number))
    for i in range(first_prime, max_possible_divisor + 1):
        if number % i == 0:
            return False
    return True


def prime_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_prime(number)
    )


game_prompt = BRAIN_PRIME_PROMPT
question_generator = generate_natural_number
input_function = yes_no_input
correct_answer_generator = prime_yes_no

__all__ = {
    'game_prompt',
    'question_generator',
    'input_function',
    'correct_answer_generator'
}
