from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number = randint(1, 100)
    question = number
    correct_answer = 'yes' if prime_number(number) else 'no'
    return correct_answer, question


def prime_number(number):
    """Predicate False or True for def prime()"""
    div = 1
    count = 1

    if number < 2 or number % 2 == 0 and number != 2:
        return False
    elif number == 2:
        return True
    else:
        while div < number and count < 3:
            result = number % div
            div += 2
            if result == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True
