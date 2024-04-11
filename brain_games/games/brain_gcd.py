import random


GAME_PROMPT = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def generate_pair_of_numbers():
    return ' '.join(str(random.randint(1, MAX_NUMBER))
                    for _ in range(2))


def calc_greatest_common_divisor(pair_of_numbers: str) -> int:
    numbers = [int(n) for n in pair_of_numbers.split(' ')]
    while numbers[0] != numbers[1]:
        if numbers[0] > numbers[1]:
            numbers[0] = numbers[0] - numbers[1]
        else:
            numbers[1] = numbers[1] - numbers[0]
    return numbers[0]


def question_answer_generator():
    question = generate_pair_of_numbers()
    answer = calc_greatest_common_divisor(question)
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
