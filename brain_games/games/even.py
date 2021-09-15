from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def round():
    number = randint(1, 100)
    question = number
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return correct_answer, question
