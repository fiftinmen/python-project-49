import prompt

MAX_ATTEMPTS_COUNT = 3


def run_game(game_module) -> None:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
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
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
