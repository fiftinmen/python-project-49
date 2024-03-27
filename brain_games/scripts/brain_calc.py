#!/usr/bin/env python3

from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import integer_input
from brain_games.scripts.games.calc_game import (generate_expression,
                                                 evaluate_expression,
                                                 BRAIN_CALC_PROMPT
                                                 )


def main():
    game(
        game_prompt=BRAIN_CALC_PROMPT,
        input_function=integer_input,
        question_generator=generate_expression,
        correct_answer_generator=evaluate_expression
        )


if __name__ == '__main__':
    main()
