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

    correct_answer = str(getHidden_number(number, step))

    question = get_progression(number, step).replace(correct_answer, '..', 1)

    return correct_answer, question


def getHidden_number(number, step):
    """Generate hide random number"""
    lenProgression = LENGHT_OF_PROGRESSION

    lastNumber = number + step * (lenProgression - 1)
    hidden_number = randrange(number, lastNumber, step)

    return hidden_number


def get_progression(number, step):
    """Generate list of number for progression"""

    progression = ''
    count = LENGHT_OF_PROGRESSION
    nextNumber = number

    while count:
        progression = progression + str(nextNumber) + ' '
        nextNumber = nextNumber + step
        count -= 1
    return progression
