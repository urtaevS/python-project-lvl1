import random

from brain_games.games.variables import wrong_answer

from brain_games.games.greeting import greeting


def progression():
    """Guess the missing number from tuple"""
    name = greeting()
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
    print('Congratulations, {0}!'.format(name))
