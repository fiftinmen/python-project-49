from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import (bool_to_yes_no,
                                                    is_prime,
                                                    yes_no_input,
                                                    generate_natural_number
                                                    )


def prime_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_prime(number)
    )


BRAIN_PRIME_PROMPT = 'Answer "yes" if given number is prime. '\
    + 'Otherwise answer "no".'


def brain_prime():
    game(
        game_prompt=BRAIN_PRIME_PROMPT,
        input_function=yes_no_input,
        question_generator=generate_natural_number,
        correct_answer_generator=prime_yes_no
    )
