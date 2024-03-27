#!/usr/bin/env python3

from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import integer_input
from brain_games.scripts.games.progression_game import (generate_progression,
                                                        calc_missing_element,
                                                        BRAIN_PROGRESSION_PROMPT
                                                        )


def main():
    game(
        game_prompt=BRAIN_PROGRESSION_PROMPT,
        input_function=integer_input,
        question_generator=generate_progression,
        correct_answer_generator=calc_missing_element
        )


if __name__ == '__main__':
    main()
