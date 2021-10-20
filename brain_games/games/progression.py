from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'


def generate_game_data():
    number = randint(1, 100)
    step = randint(1, 5)

    return number, step


def get_question_and_answer():
    number, step = generate_game_data()

    correct_answer, row_of_numbers = answer(number, step)

    question = row_of_numbers.replace(str(correct_answer), '..', 1)

    return correct_answer, question


def answer(number, step):
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
