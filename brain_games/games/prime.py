from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number1 = randint(1, 100)
    question = number1
    correct_answer = 'yes' if prime_num(number1) else 'no'
    return correct_answer, question


def prime_num(number1):
    """Predicate False or True for def prime()"""
    div = 1
    count = 1

    if number1 < 2 or number1 % 2 == 0 and number1 != 2:
        return False
    elif number1 == 2:
        return True
    else:
        while div < number1 and count < 3:
            result = number1 % div
            div += 2
            if result == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True
