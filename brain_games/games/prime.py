import random

from brain_games.games.variables import wrong_answer

from brain_games.games.greeting import greeting


def prime():
    """Find a prime number"""
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        print('Question: {0}'.format(num))
        answer = input(str('Your answer: '))
        right_answer = 'yes' if prime_num(num) else 'no'
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulations, {0}!'.format(name))


def prime_num(num):
    """Predicate False or True for def prime()"""
    div = 1
    count = 1
    if num < 2 or num % 2 == 0 and num != 2:
        return False
    elif num == 2:
        return True
    else:
        while div < num and count < 3:
            result = num % div
            div += 2
            if result == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True
