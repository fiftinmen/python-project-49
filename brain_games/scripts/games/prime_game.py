from brain_games.scripts.games.common_logic import (bool_to_yes_no,
                                                    is_prime)


def prime_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_prime(number)
        )


BRAIN_PRIME_PROMPT = 'Answer "yes" if given number is prime.'\
    + ' Otherwise answer "no".'
