#!/usr/bin/env python3
from brain_games.game_engine import game
from brain_games.games.progression_game import brain_progression


def main():
    game(**brain_progression())


if __name__ == '__main__':
    main()
