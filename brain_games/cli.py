import prompt


def greeting():
    """Get an user name and greeting user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
