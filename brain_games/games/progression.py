"""Find a missing number in progression"""

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

    correct_answer = str(getHide_number(number, step))

    question = get_progression(number, step).replace(correct_answer, '..', 1)

    return correct_answer, question


def getHide_number(number, step):
    """Generate hide random number"""

    lastNumber = number + step * (10 - 1)
    hide_number = randrange(number, lastNumber, step)

    return hide_number


def get_progression(number, step):
    """Generate list of number for progression"""

    progression = ''
    lenProgression = LENGHT_OF_PROGRESSION
    nextNumber = number

    while lenProgression:
        progression = progression + str(nextNumber) + ' '
        nextNumber = nextNumber + step
        lenProgression -= 1
    return progression
