#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import gcd


def main():
    """Start calling two func."""
    engine.run(gcd.get_question_and_answer, gcd.DESCRIPTION)


if __name__ == '__main__':
    main()
