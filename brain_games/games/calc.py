import random

from brain_games.games.variables import wrong_answer

from brain_games.games.greeting import greeting


def calc():
    """Calculate two random numbers."""
    name = greeting()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        simbol = random.choice(['+', '-', '*'])
        term = '{0} {1} {2}'.format(num1, simbol, num2)
        print('Question: {0}'.format(term))
        answer = input('Your answer: ')
        if simbol == '+':
            right_answer = num1 + num2
        elif simbol == '-':
            right_answer = num1 - num2
        elif simbol == '*':
            right_answer = num1 * num2
        if answer == str(right_answer):
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
