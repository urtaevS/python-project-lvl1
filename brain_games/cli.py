import prompt


def welcome_user():
    """Get an user name and promt user."""
    greeting()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def greeting():
    """Greeting an user."""
    print('Welcome to the Brain Games!')
