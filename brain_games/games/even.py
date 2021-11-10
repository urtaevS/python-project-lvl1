"""Check random number for evenness"""

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data():
    """Generate random number between 1 and 100"""

    number = randint(1, 100)
    return number


def get_question_and_answer():
    """Collect 'question' and 'correct_answer' for games"""

    number = generate_game_data()
    question = number
    correct_answer = 'yes' if is_even(number) is False else 'no'
    return correct_answer, question


def is_even(number):
    """Check variable 'number' for even"""

    return bool(number % 2)
