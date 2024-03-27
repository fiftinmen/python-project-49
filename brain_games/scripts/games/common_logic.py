import prompt
import random

MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def is_prime(number: int) -> str:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def bool_to_yes_no(true: bool) -> str:
    return 'yes' if true else 'no'


def integer_input():
    return prompt.integer(prompt='Your answer: ', empty=False)


def generate_number():
    return random.randint(-MAX_NUMBER, MAX_NUMBER)


def generate_natural_number():
    return random.randint(1, MAX_NUMBER)


def format_integer(number):
    return str(number)


def parse_integer(formatted_integer: str):
    return int(formatted_integer)


def parse_expression(expression):
    expression_parts = expression.split(' ')
    expression_members = []
    operations = []
    for i, part in enumerate(expression_parts):
        if not is_even(i + 1):
            expression_members.append(parse_integer(part))
        else:
            operations.append(part)
    return expression_members, operations


YES_NO_PATTERN = r'(yes)|(no)'


def yes_no_input():
    answer = prompt.regex(YES_NO_PATTERN, prompt='Your answer: ', empty=False)
    answer = answer.groups()
    # получили массив из двух элементов:
    # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
    return answer[0] if answer[0] else answer[1]
