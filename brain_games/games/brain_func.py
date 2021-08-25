import random

import prompt

from brain_games.games.variables import wrong_answer, welcome


def greeting():
    """Greeting an user and a name."""
    print(welcome)
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def even():
    """Ask user and start the game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        print('Question: {0}'.format(num))
        answer = input(str('Your answer: '))
        right_answer = 'yes' if num % 2 == 0 else 'no'
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulation, {0}!'.format(name))


def calc():
    """Calculate random numbers."""
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        simbol = random.choice(['+', '-', '*'])
        term = '{0} {1} {2}'.format(num1, simbol, num2)
        print('Question: {0}'.format(term))
        answer = input(str('Your answer: '))
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
    print('Congratulation, {0}!'.format(name))


def gcd():
    """Find the greatest common divisor."""
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
    print('Congratulation, {0}!'.format(name))
