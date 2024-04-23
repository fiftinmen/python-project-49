import random


GAME_PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    question = random.randint(-MAX_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'generate_question_and_answer',
}
