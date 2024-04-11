import prompt

MAX_ATTEMPTS_COUNT = 3


def run_game(game_module) -> None:
    game_prompt = game_module.GAME_PROMPT
    question_answer_generator = game_module.question_answer_generator
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_prompt)
    for _ in range(MAX_ATTEMPTS_COUNT):
        question, correct_answer = question_answer_generator()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
