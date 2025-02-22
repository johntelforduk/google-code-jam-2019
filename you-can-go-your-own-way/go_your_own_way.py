# Solution to second qualification problem, "You Can Go Your Own Way".
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

from sys import stdin, argv
from random import random

DEBUG_ENABLED = "-d" in argv


def debug(msg):
    if DEBUG_ENABLED:
        print("Debug: {}".format(msg))


num_cases = int(stdin.readline())
debug('num_cases = ' + str(num_cases))

for case in range(1, num_cases + 1):
    n = int(stdin.readline())
    debug('n =' + str(n))

    lydia = stdin.readline().strip()
    debug('lydia =' + lydia)

    solved = False
    attempt = ''
    while not solved:
        # First, make a dictionary of Lydia's steps
        lydia_steps = {}                    # Key=(x, y) coordinates of current position, Value=Move she made.
        x, y = 0, 0

        for step in lydia:
            debug('step = ' + step)
            lydia_steps[(x, y)] = step

            if step == 'E':
                x += 1
            else:                           # If not 'E', it must be 'S'.
                y += 1

        while not solved:
            attempt = ''                    # New attempt.
            x, y = 0, 0                     # Attempt starts at the origin.
            for step in lydia:              # Solution will have same number of steps as Lydis'a walk.
                # Pick the next move.
                if x == (n - 1):            # Can't go any further East, so next move must be South.
                    next_move = 'S'
                elif y == (n - 1):          # Can't go any further South, so next move must be East.
                    next_move = 'E'
                else:                       # Either direction possible, so pick a random one.
                    if random() < 0.5:
                        next_move = 'E'
                    else:
                        next_move = 'S'

                # Check if the next_move is same as Lydia's move.
                if (x, y) in lydia_steps:
                    if lydia_steps[(x, y)] == next_move:
                        break

                # Make the move.
                if next_move == 'E':
                    x += 1
                else:
                    y += 1
                attempt += next_move

            if len(attempt) == len(lydia_steps):
                solved = True

            debug('attempt = ' + attempt)

    print("Case #{}: {}".format(case, attempt))
