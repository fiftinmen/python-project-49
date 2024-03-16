import prompt


def game(rules: str,
         question_generator: callable,
         correct_answer_generator: callable,
         input_function: callable) -> None:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(rules)
    for _ in range(3):
        question = question_generator()
        correct_answer = correct_answer_generator(question)
        print(f'Question: {question}')
        answer = input_function()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was " +
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
