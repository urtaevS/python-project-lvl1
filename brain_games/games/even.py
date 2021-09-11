import random

import prompt


from brain_games.games.variables import wrong_answer, question


def core():
    """Get an user name and promt user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(question)
    count = 0
    while count < 3:
        right_answer, answer = even()
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(wrong_answer.format(answer, right_answer, name))
            return
    print('Congratulations, {0}!'.format(name))


def even():
    num = random.randint(1, 100)
    print('Question: {0}'.format(num))
    right_answer = 'yes' if num % 2 == 0 else 'no'
    answer = input(str('Your answer: '))
    return right_answer, answer
