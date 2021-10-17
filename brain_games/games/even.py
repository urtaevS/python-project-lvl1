from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data():
    number = randint(1, 100)
    return number


def receive_question_and_answer():
    question = generate_game_data()
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, question
