import random

import prompt


def main():
    """Start calling two func."""
    greeting()
    even()


def greeting():
    """Greeting an user."""
    print('Welcome to the Brain Games!')


def even():
    """Prompt user name and start the game."""
    count = 0
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        num = random.randint(0, 100)
        print('Question: {0}'.format(num))
        answer = input(str('Your answer: '))
        right_answer = 'yes' if num % 2 == 0 else 'no'
        if answer != right_answer:
            print("'{0}' is wrong answer ;(.Correct answer was '{1}'.".format(answer, right_answer) + "\nLet's try again, {0}!".format(name))
            break
        else:
            print('Correct!')
            count += 1
        print('Congratilation, {0}!'.format(name))


if __name__ == '__main__':
    main()
