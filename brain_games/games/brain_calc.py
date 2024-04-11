import random


GAME_PROMPT = 'What is the result of the expression?'


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

MAX_NUMBER = 100


def generate_number_sequence():
    return [random.randint(-MAX_NUMBER, MAX_NUMBER)
            for _ in range(EXPRESSION_MEMBERS_COUNT)]


def generate_expression():
    expression_members_list = generate_number_sequence()
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
    numbers = []
    operations = []
    for i, part in enumerate(expression_parts):
        if i % 2 == 0:
            numbers.append(parse_integer(part))
        else:
            operations.append(part)
    return numbers, operations


def evaluate_expression(expression):
    numbers, operations = parse_expression(expression)
    for operation in OPERATIONS_ORDER:
        apply_operation(numbers, operations, operation)
    return numbers[0]


def question_answer_generator():
    question = generate_expression()
    answer = evaluate_expression(question)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
