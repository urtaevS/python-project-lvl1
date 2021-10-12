from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'


def generate_numbers():
    number = randint(1, 100)
    step = randint(1, 5)

    return number, step


def generate_game_data():
    number, step = generate_numbers()

    row_of_numbers = ''
    buffer_number = number
    length_row_of_numbers = 0

    for length_row_of_numbers in range(10):
        row_of_numbers = row_of_numbers + str(buffer_number) + ' '
        last_number = buffer_number + step
        buffer_number = last_number
        length_row_of_numbers += 1
    correct_answer = str(randrange(number, last_number, step))
    question = row_of_numbers.replace(correct_answer, '..')

    return correct_answer, question
