import random

from brain_games.games.variables import wrong_answer

from brain_games.games.greeting import greeting


def even():
    """Guess the even number"""
    name = greeting()
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
    print('Congratulations, {0}!'.format(name))
