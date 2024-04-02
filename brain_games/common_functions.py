import prompt
import random

MAX_NUMBER = 100


def bool_to_yes_no(true: bool) -> str:
    return "yes" if true else "no"


def integer_input():
    return prompt.integer(prompt="Your answer: ", empty=False)


def generate_number(min_number=-MAX_NUMBER, max_number=MAX_NUMBER):
    return random.randint(min_number, max_number)


def generate_natural_number():
    return generate_number(1, MAX_NUMBER)


def generate_number_sequence(
        length,
        min_number=(-MAX_NUMBER),
        max_number=MAX_NUMBER
):
    return [generate_number(min_number, max_number) for _ in range(length)]


YES_NO_PATTERN = r"(yes)|(no)"


def yes_no_input():
    answer = prompt.regex(YES_NO_PATTERN, prompt="Your answer: ", empty=False)
    answer = answer.groups()
    # получили массив из двух элементов:
    # ['yes', Nonetype] или [NoneType, 'no] в зависимости от ответа
    return answer[0] if answer[0] else answer[1]
