from brain_games.common_functions import (bool_to_yes_no,
                                          yes_no_input,
                                          generate_number,
                                          )


def is_even(number):
    return number % 2 == 0


def even_yes_no(number: int) -> str:
    return bool_to_yes_no(
        is_even(number)
    )


BRAIN_EVEN_PROMPT = 'Answer "yes" if the number is even, '\
    + 'otherwise answer "no".'


def brain_even():
    return {
        "game_prompt": BRAIN_EVEN_PROMPT,
        "question_generator": generate_number,
        "input_function": yes_no_input,
        "correct_answer_generator": even_yes_no
    }
