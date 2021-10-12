#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import progression


def main():
    """Start calling two func."""
    engine.run(progression.generate_game_data)


if __name__ == '__main__':
    main()
