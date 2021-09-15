import prompt


def welcome_user():
    """Get an user name and promt user."""
    greeting()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def greeting():
    """Greeting an user."""
    print('Welcome to the Brain Games!')