#!/usr/bin/env python3
from brain_games.game_engine import game
from brain_games.games.gcd_game import brain_gcd


def main():
    game(**brain_gcd())


if __name__ == '__main__':
    main()
