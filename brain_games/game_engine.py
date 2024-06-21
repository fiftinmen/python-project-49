import prompt
from brain_games.games import brain_even
from brain_games.games import brain_calc
from brain_games.games import brain_prime
from brain_games.games import brain_progression
from brain_games.games import brain_gcd

MAX_ATTEMPTS_COUNT = 3


def choose_game() -> None:
    print('Choose game to play:',
          'a) brain-even: determine whether a number is even or not ',
          'b) brain-prime: is number is prime or not',
          'c) brain-gcd: find the greatest common divisor of two number',
          'd) brain-progression: find missed member of arithmetic progression',
          'e) brain-calc: find the result of arithmetic expression',
          'x) exit brain-games',
          sep='\n')
    answer = ''
    while answer not in {'a', 'b', 'c', 'd', 'e', 'x'}:
        answer = prompt.character('Your choice: ',)
    return {'a': brain_even,
            'b': brain_prime,
            'c': brain_gcd,
            'd': brain_progression,
            'e': brain_calc,
            'x': None}.get(answer)


def run_game(game_module, user_name) -> None:
    print(game_module.GAME_PROMPT)
    for _ in range(MAX_ATTEMPTS_COUNT):
        question, correct_answer = \
            game_module.generate_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


def good_bye():
    print('See you later, {username}!')


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    return user_name


def run_brain_games() -> None:
    user_name = welcome_user()
    if game_module := choose_game():
        run_game(game_module, user_name)
    else:
        good_bye(user_name)
