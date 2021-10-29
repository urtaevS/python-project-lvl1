"""Generate an string of progression"""

from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'

LENGHT_OF_PROGRESSION = 10

def generate_game_data():
    """Generate random number between 1 and 100"""
    number = randint(1, 100)
    step = randint(1, 5)

    return number, step


def get_question_and_answer():
    """Collect 'question' and 'correct_answer' for games"""

    number, step = generate_game_data()

    correct_answer, row_of_numbers = calculate(number, step)

    question = row_of_numbers.replace(str(correct_answer), '..', 1)

    return correct_answer, question

def generate_progression(number, step):
    row_of_numbers = ''
    while LENGHT_OF_PROGRESSION:

def calculate(number, step):
    row_of_numbers = ''
    buffer_number = number
    length_row_of_numbers = 0

    for length_row_of_numbers in range(10):
        row_of_numbers = row_of_numbers + str(buffer_number) + ' '
        last_number = buffer_number + step
        buffer_number = last_number
        length_row_of_numbers += 1
    correct_answer = str(randrange(number, last_number, step))
    return str(correct_answer), row_of_numbers
