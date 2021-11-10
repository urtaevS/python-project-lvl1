"""Check random number is prime"""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game_data():
    """Generate random number between 1 and 100"""

    number = randint(1, 100)

    return number


def get_question_and_answer():
    """Collect 'question' and 'correct_answer' for games"""

    number = generate_game_data()
    print(number)
    question = number
    print(question)
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    print(correct_answer)
    return correct_answer, question


def is_prime(number):
    """Check variable 'number' prime or not"""

    divider_number = 1
    divide_count = 1

    if number < 2 or number % 2 == 0 and number != 2:
        return False
    elif number == 2:
        return True
    else:
        while divider_number < number and divide_count < 3:
            result = number % divider_number
            divider_number += 2
            if result == 0:
                divide_count += 1
        if divide_count > 2:
            return False
        else:
            return True
