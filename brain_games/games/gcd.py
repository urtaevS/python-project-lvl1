from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    while number2 > 0:
        result = number1 % number2
        number1 = number2
        number2 = result
    correct_answer = number1

    return str(correct_answer), question
