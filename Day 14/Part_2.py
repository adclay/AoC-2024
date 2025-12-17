from Puzzle_Input import *
import time

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

"""
To solve this, I ran the code below starting at t = 0 and incrementing t by 1. I noticed a vertical
pattern appeared at times t = 103, 204, and 305. So I modified the start time to t = 103 and
incremented t by 101 until the Christmas tree appeared at t = 6870.
"""

def print_grid(grid, size):
    for y in range(size[1]):
        for x in range(size[0]):
            print(grid[x, y], end='')
        print()
    print()

t = 103
while True:
    print(f"Time = {t}:")

    pos = (robots[:, :2] + t * robots[:, 2:]) % np.array(size)
    grid = np.full(size, '.', dtype = str)
    grid[pos[:, 0], pos[:, 1]] = '#'
    print_grid(grid, size)

    t += 101
    time.sleep(.5)
