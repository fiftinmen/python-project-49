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
    numbers = generate_number_sequence()
    operations = [
        OPERATION_TYPES[random.randint(1, OPERATION_TYPES_COUNT)]
        for _ in range(OPERATIONS_COUNT)
    ]
    expression = str(numbers[0])
    for i, member in enumerate(numbers[1:]):
        expression = f' {operations[i]} '.join([expression, str(member)])
    return numbers, operations, expression


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


def evaluate_expression(numbers, operations):
    for operation in OPERATIONS_ORDER:
        apply_operation(numbers, operations, operation)
    return numbers[0]


def question_answer_generator():
    numbers, operations, question = generate_expression()
    answer = evaluate_expression(numbers, operations)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
