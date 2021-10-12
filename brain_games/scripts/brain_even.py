#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import even


def main():
    """Start even game."""
    engine.run(even.get_question_and_correct_answer)


if __name__ == '__main__':
    main()
