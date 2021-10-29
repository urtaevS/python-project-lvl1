"""Find the greatest common divisor of given numbers."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game_data():
    """Generate two random numbers between 1 and 100"""
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    return number1, number2


def get_question_and_answer():
    """Collect 'question' and 'correct_answer' for games"""
    number1, number2 = generate_game_data()

    question = f'{number1} {number2}'
    correct_answer = getGcd(number1, number2)

    return str(correct_answer), question


def getGcd(number1, number2):
    """Find the greatest common divisor for two numbers"""
    while number2 > 0:
        result = number1 % number2
        number1 = number2
        number2 = result
    correct_answer = number1

    return str(correct_answer)
