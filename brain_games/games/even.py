import random


def even():
    num = random.randint(1, 100)
    print('Question: {0}'.format(num))
    right_answer = 'yes' if num % 2 == 0 else 'no'
    answer = input(str('Your answer: '))
    return right_answer, answer
