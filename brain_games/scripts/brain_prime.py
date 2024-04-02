#!/usr/bin/env python3
from brain_games.game_engine import game
from brain_games.games.prime_game import brain_prime


def main():
    game(**brain_prime())


if __name__ == '__main__':
    main()
