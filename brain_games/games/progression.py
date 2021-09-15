from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'


def round():
    replace_number = '..'
    number = randint(1, 100)
    step = randint(1, 5)
    string = ''
    buffer_number = number
    length_string = 0

    for length_string in range(10):
        string = string + str(buffer_number) + ' '
        last_number = buffer_number + step
        buffer_number = last_number
        length_string += 1
    correct_answer = randrange(number, last_number, step)
    correct_answer = str(correct_answer)
    string_replace = string.replace(correct_answer, replace_number)

    question = string_replace

    return correct_answer, question
