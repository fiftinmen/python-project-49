import prompt
import random
from brain_games.game_engine import game
from brain_games.common_functions import (integer_input,
                                          generate_number_sequence
                                          )

OPERATION_TYPES = {
    1: '*',
    2: '+',
    3: '-',
}

OPERATIONS_ORDER = {
    '*': 0,
    '-': 1,
    '+': 2,
}

DO_OPERATION = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}


EXPRESSION_MEMBERS_COUNT = 2
OPERATIONS_COUNT = EXPRESSION_MEMBERS_COUNT - 1
OPERATION_TYPES_COUNT = len(OPERATION_TYPES)
ORDERED_OPERATIONS = [[] for _ in range(OPERATION_TYPES_COUNT)]


def generate_expression():
    expression_members_list = generate_number_sequence(EXPRESSION_MEMBERS_COUNT)
    operations = [
        OPERATION_TYPES[random.randint(1, OPERATION_TYPES_COUNT)]
        for _ in range(OPERATIONS_COUNT)
    ]
    expression = str(expression_members_list[0])
    for i, member in enumerate(expression_members_list[1:]):
        expression = f' {operations[i]} '.join([expression, str(member)])
    print(expression)
    return expression


def apply_operation(numbers, operations, operation):
    i = 0
    while i < len(operations):
        if operations[i] == operation:
            numbers[i] = DO_OPERATION[operation](numbers[i], numbers[i + 1])
            numbers.pop(i + 1)
            operations.pop(i)
            i = 0
        else:
            i += 1


def parse_integer(formatted_integer: str):
    return int(formatted_integer)


def parse_expression(expression):
    expression_parts = expression.split(' ')
    expression_members = []
    operations = []
    for i, part in enumerate(expression_parts):
        if i % 2 == 0:
            expression_members.append(parse_integer(part))
        else:
            operations.append(part)
    return expression_members, operations


def evaluate_expression(expression):
    numbers, operations = parse_expression(expression)

    for operation in OPERATIONS_ORDER:
        apply_operation(numbers, operations, operation)

    result = numbers[0]
    return result


def brain_calc_input():
    return prompt.integer(prompt='Your answer: ', empty=False)


BRAIN_CALC_PROMPT = 'What is the result of the expression?'


def brain_calc():
    game(game_prompt=BRAIN_CALC_PROMPT,
         question_generator=generate_expression,
         input_function=integer_input,
         correct_answer_generator=evaluate_expression)
