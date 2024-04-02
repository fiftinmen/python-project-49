#!/usr/bin/env python3
from brain_games.game_engine import game
from brain_games.games.calc_game import brain_calc


def main():
    game(**brain_calc())


if __name__ == '__main__':
    main()
