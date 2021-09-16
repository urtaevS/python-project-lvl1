from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'

def round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    simbol = choice(['+', '-', '*'])

    question = f'{number1} {simbol} {number2}'

    if simbol == '+':
        correct_answer = number1 + number2
    elif simbol == '-':
        correct_answer = number1 - number2
    elif simbol == '*':
        correct_answer = number1 * number2

    return str(correct_answer), question
