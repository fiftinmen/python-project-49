import random


def generate_pair_of_numbers():
    return str(random.randint(1, 100)) + ' ' + str(random.randint(1, 100))


def calc_greatest_common_divisor(pair_of_numbers: str) -> int:
    numbers = [int(n) for n in pair_of_numbers.split(' ')]
    while numbers[0] != numbers[1]:
        if numbers[0] > numbers[1]:
            numbers[0] = numbers[0] - numbers[1]
        else:
            numbers[1] = numbers[1] - numbers[0]
    return numbers[0]


BRAIN_GCD_PROMPT = 'Find the greatest common divisor of given numbers.'
