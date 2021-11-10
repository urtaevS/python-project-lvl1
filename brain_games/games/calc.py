"""Calculate an expression between two numbers"""

from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = ['+', '-', '*']


def generate_game_data():
    """Generate two random numbers and operator"""

    number1 = randint(1, 100)
    number2 = randint(1, 100)

    operator = choice(OPERATORS)

    return number1, number2, operator


def get_question_and_answer():
    """Collect 'question' and 'correct_answer' for games"""

    number1, number2, operator = generate_game_data()

    question = f'{number1} {operator} {number2}'
    correct_answer = calculate(operator, number1, number2)

    return str(correct_answer), question


def calculate(operator, number1, number2):
    """Evaluate an expression between two numbers"""

    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '*':
        correct_answer = number1 * number2

    return correct_answer
