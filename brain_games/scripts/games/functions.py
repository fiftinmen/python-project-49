import prompt
import random


def integer_input():
    return prompt.integer(prompt='Your answer: ', empty=False)


def generate_number():
    return random.randint(-1000, 1000)


def generate_natural_number():
    return random.randint(1, 1000)


def yes_no_input():
    pattern = r'(yes)|(no)'
    answer = prompt.regex(pattern, prompt='Your answer: ', empty=False)
    answer = answer.groups()
    # получили массив из двух элементов:
    # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
    return answer[0] if answer[0] else answer[1]