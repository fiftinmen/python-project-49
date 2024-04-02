from brain_games.common_functions import (
    integer_input,
    generate_number_sequence,
)


PAIR_LENGTH = 2


def generate_pair_of_numbers():
    return ' '.join(str(number)
                    for number in generate_number_sequence(
                        PAIR_LENGTH,
                        min_number=1)
                    )


def calc_greatest_common_divisor(pair_of_numbers: str) -> int:
    numbers = [int(n) for n in pair_of_numbers.split(' ')]
    while numbers[0] != numbers[1]:
        if numbers[0] > numbers[1]:
            numbers[0] = numbers[0] - numbers[1]
        else:
            numbers[1] = numbers[1] - numbers[0]
    return numbers[0]


BRAIN_GCD_PROMPT = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    return {
        "game_prompt": BRAIN_GCD_PROMPT,
        "question_generator": generate_pair_of_numbers,
        "input_function": integer_input,
        "correct_answer_generator": calc_greatest_common_divisor
    }
