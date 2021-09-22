from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_numbers_and_simbol():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    simbol = choice(['+', '-', '*'])

    return number1, number2, simbol


def get_question_and_correct_answer():
    number1, number2, simbol = generate_numbers_and_simbol()

    question = f'{number1} {simbol} {number2}'

    if simbol == '+':
        correct_answer = number1 + number2
    elif simbol == '-':
        correct_answer = number1 - number2
    elif simbol == '*':
        correct_answer = number1 * number2

    return str(correct_answer), question
