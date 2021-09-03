import random

from brain_games.games.variables import wrong_answer

from brain_games.games.greeting import greeting


def gcd():
    """Find the greatest common divisor of two random numbers."""
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        term = '{0} {1}'.format(num1, num2)
        print('Question: {0}'.format(term))
        answer = input(str('Your answer: '))
        while num2 > 0:
            result = num1 % num2
            num1 = num2
            num2 = result
        right_answer = num1
        if answer == str(right_answer):
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
