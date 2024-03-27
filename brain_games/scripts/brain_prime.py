#!/usr/bin/env python3

from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import (yes_no_input,
                                                    generate_natural_number
                                                    )
from brain_games.scripts.games.prime_game import (prime_yes_no,
                                                  BRAIN_PRIME_PROMPT
                                                  )


def main():
    game(
        game_prompt=BRAIN_PRIME_PROMPT,
        input_function=yes_no_input,
        question_generator=generate_natural_number,
        correct_answer_generator=prime_yes_no
        )


if __name__ == '__main__':
    main()
