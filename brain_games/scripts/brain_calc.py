#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import calc


def main():
    """Start playing game."""
    engine.run(calc.get_question_and_correct_answer)


if __name__ == '__main__':
    main()
