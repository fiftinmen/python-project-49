#!/usr/bin/env python3


import prompt
import random


def even_yes_or_no(number: int) -> bool:
    return 'yes' if number % 2 == 0 else 'no'


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(-1000, 1000)
        correct_answer = even_yes_or_no(number)
        print(f'Question: {number}')
        pattern = r'(yes)|(no)'
        answer = prompt.regex(pattern, prompt='Your answer: ', empty=False)
        answer = answer.groups()
        # возвращает массив из двух элементов:
        # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
        answer = answer[0] if answer[0] else answer[1]
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was " +
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
