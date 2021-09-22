from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_numbers():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    return number1, number2


def get_question_and_correct_answer():
    number1, number2 = generate_numbers()

    question = f'{number1} {number2}'

    while number2 > 0:
        result = number1 % number2
        number1 = number2
        number2 = result
    correct_answer = number1

    return str(correct_answer), question
