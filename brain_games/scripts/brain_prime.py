#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import prime


def main():
    """Start calling two func."""
    engine.run(prime.receive_question_and_answer, prime.DESCRIPTION)


if __name__ == '__main__':
    main()
