#!/usr/bin/env python3
from brain_games import engine

from brain_games.games import gcd


def main():
    """Start calling two func."""
    engine.run(gcd.round)


if __name__ == '__main__':
    main()
