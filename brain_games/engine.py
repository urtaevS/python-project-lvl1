
import prompt

ROUND_COUNTER = 3


def run(round):
    """Get an user name and greeting user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = ROUND_COUNTER
    while count:
        correct_answer, question = round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        RESULT = f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
        if correct_answer != answer:
            print(RESULT)
            print(f'Let\'s try again, {name}!')
            return
        else:
            print('Correct!')
            count -= 1
    print(f'Congratulations, {name}!')
