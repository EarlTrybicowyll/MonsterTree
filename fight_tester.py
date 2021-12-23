#!/usr/bin/python3
from engine import run

import sys


def main():
    args = sys.argv
    run(initial_inputs=args[1:])


if __name__ == "__main__":
    main()
