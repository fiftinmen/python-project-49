import prompt
import random

MAX_NUMBER = 100

def integer_input():
    return prompt.integer(prompt='Your answer: ', empty=False)


def generate_number():
    return random.randint(-MAX_NUMBER, MAX_NUMBER)


def generate_natural_number():
    return random.randint(1, MAX_NUMBER)


def yes_no_input():
    pattern = r'(yes)|(no)'
    answer = prompt.regex(pattern, prompt='Your answer: ', empty=False)
    answer = answer.groups()
    # получили массив из двух элементов:
    # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
    return answer[0] if answer[0] else answer[1]