import prompt
import random


def main():
    greeting()
    even()

def greeting():
    print('Welcome to the Brain Games!')

def even():
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = random.randint(1,100)
        print(f'Question: {num}')
        answer = input(str('Your answer: '))
        right_answer = 'yes' if num % 2 == 0 else 'no'
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
            Let's try again, {name}!""")
            i = 0
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()