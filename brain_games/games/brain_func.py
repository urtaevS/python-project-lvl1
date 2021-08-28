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
    """Guess the even number"""
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
    """Calculate two random numbers."""
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
    print('Congratulation, {0}!'.format(name))


def gcd():
    """Find the greatest common divisor of two random numbers."""
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


def progression():
    """Guess the missing number from tuple"""
    print('What number is missing in the progression?')
    replace_num = '..'
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        step = random.randint(1, 5)
        string = ''
        temp_num1 = num1
        i = 0
        for i in range(10):
            string = string + str(temp_num1) + ' '
            fin = temp_num1 + step
            temp_num1 = fin
            i += 1
        right_answer = random.randrange(num1, fin, step)
        right_answer = str(right_answer)
        string_replace = string.replace(right_answer, replace_num)
        print('Question: {0}'.format(string_replace))
        answer = input('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulation, {0}!'.format(name))


def prime():
    """Find a prime number"""
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
    print('Congratulation, {0}!'.format(name))


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
