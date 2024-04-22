import random


GAME_PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100


def question_answer_generator():
    question = random.randint(-MAX_NUMBER, MAX_NUMBER)
    answer = question % 2 == 0
    return question, answer


__all__ = {
    'GAME_PROMPT',
    'question_answer_generator',
}
