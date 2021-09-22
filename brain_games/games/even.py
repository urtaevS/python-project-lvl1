from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    number = randint(1, 100)
    return number


def get_question_and_correct_answer():
    question = generate_number()
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, question
