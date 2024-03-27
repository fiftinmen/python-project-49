#!/usr/bin/env python3

from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import (yes_no_input,
                                                    generate_number,
                                                    )
from brain_games.scripts.games.even_game import (even_yes_no,
                                                 BRAIN_EVEN_PROMPT
                                                 )


def main():
    game(
        game_prompt=BRAIN_EVEN_PROMPT,
        input_function=yes_no_input,
        question_generator=generate_number,
        correct_answer_generator=even_yes_no
        )


if __name__ == '__main__':
    main()
