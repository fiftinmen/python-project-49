#!/usr/bin/env python3
from brain_games.game_engine import game
from brain_games.games.even_game import brain_even


def main():
    game(**brain_even())


if __name__ == '__main__':
    main()
