import random

import prompt


def greeting():
    """Greeting an user."""
    print('Welcome to the Brain Games!')


def even():
    """Prompt user name and start the game."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(0, 100)
        print('Question: {0}'.format(num))
        answer = input(str('Your answer: '))
        right_answer = 'yes' if num % 2 == 0 else 'no'
        wrong_answer = "'{0}' is wrong answer ;(.Correct answer was '{1}'.".format(answer, right_answer) + "\nLet's try again, {0}!".format(name)
        if answer != right_answer:
            print(wrong_answer)
            break
        else:
            print('Correct!')
            count += 1
        print('Congratilation, {0}!'.format(name))


def calc():
    """Calculate random numbers."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    count = 0
    while count < 3:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        simbol = random.choice(['+', '-', '*'])
        expression = '{0} {1} {2}'.format(num1, simbol, num2)
        print('What is the result of the expression?')
        print('Question: {0}'.format(expression))
        answer = input(str('Your answer: '))
        if simbol == '+':
            right_answer = num1 + num2
        elif simbol == '-':
            right_answer = num1 - num2
        elif simbol == '*':
            right_answer = num1 * num2
        if answer != str(right_answer):
            print("'{0}' is wrong answer ;(.Correct answer was '{1}'.".format(answer, right_answer) + "\nLet's try again, {0}!".format(name))
            break
        else:
            print('Correct!')
            count += 1
        print('Congratilation, {0}!'.format(name))
