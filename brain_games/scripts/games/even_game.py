from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import (bool_to_yes_no,
                                                    is_even,
                                                    yes_no_input,
                                                    generate_number,
                                                    )


def even_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_even(number)
    )


BRAIN_EVEN_PROMPT = 'Answer "yes" if the number is even, '\
    + 'otherwise answer "no".'


def brain_even():
    game(
        game_prompt=BRAIN_EVEN_PROMPT,
        input_function=yes_no_input,
        question_generator=generate_number,
        correct_answer_generator=even_yes_no
    )
