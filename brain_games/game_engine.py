import prompt
from importlib import import_module

MAX_ATTEMPTS_COUNT = 3
PATH_TO_GAMES = 'brain_games.games'


def import_game(game_name: str) -> None:
    module_name = f'.{game_name}'
    game_module = import_module(module_name, PATH_TO_GAMES)
    return game_module.game_prompt, game_module.question_generator, \
        game_module.correct_answer_generator, game_module.input_function


def game(game_name: str) -> None:
    game_prompt, question_generator, \
        correct_answer_generator, input_function = import_game(game_name)
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_prompt)
    for _ in range(MAX_ATTEMPTS_COUNT):
        question = question_generator()
        correct_answer = correct_answer_generator(question)
        print(f'Question: {question}')
        answer = input_function()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  + f"'{correct_answer}'.\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
