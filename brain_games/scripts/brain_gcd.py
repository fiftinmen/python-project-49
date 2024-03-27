#!/usr/bin/env python3

from brain_games.scripts.games.game_engine import game
from brain_games.scripts.games.common_logic import integer_input
from brain_games.scripts.games.gcd_game import (BRAIN_GCD_PROMPT,
                                                generate_pair_of_numbers,
                                                calc_greatest_common_divisor
                                                )


def main():
    game(
        game_prompt=BRAIN_GCD_PROMPT,
        input_function=integer_input,
        question_generator=generate_pair_of_numbers,
        correct_answer_generator=calc_greatest_common_divisor
        )


if __name__ == '__main__':
    main()
