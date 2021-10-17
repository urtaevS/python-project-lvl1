from prompt import string

ROUND_COUNTER = 3


def run(receive_question_and_answer, DESCRIPTION):
    """Get an user name and greeting user. Start the game"""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    count = ROUND_COUNTER
    while count:
        correct_answer, question = receive_question_and_answer()
        print(f'Question: {question}')
        answer = string('Your answer: ')
        if correct_answer != answer:
            print(f'"{answer}"  is wrong answer ;(.'
                  f' Correct answer was "{correct_answer}" .')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
        count -= 1
    print(f'Congratulations, {name}!')
