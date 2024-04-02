import prompt

MAX_ATTEMPTS_COUNT = 3


def game(game_prompt: str,
         question_generator: callable,
         correct_answer_generator: callable,
         input_function: callable) -> None:
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
