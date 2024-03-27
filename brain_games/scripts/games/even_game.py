from brain_games.scripts.games.common_logic import (bool_to_yes_no,
                                                    is_even)


def even_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_even(number)
        )


BRAIN_EVEN_PROMPT = 'Answer "yes" if given number is even.'\
    + ' Otherwise answer "no".'
