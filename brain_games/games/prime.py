from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game_data():
    number = randint(1, 100)

    return number


def get_question_and_answer():
    number = generate_game_data()
    question = number
    correct_answer = calculate(number)

    return correct_answer, question


def calculate(number):
    correct_answer = 'yes' if calculate_prime_number(number) else 'no'

    return correct_answer


def calculate_prime_number(number):
    """Predicate False or True for def prime()"""
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
