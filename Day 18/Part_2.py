from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

"""
It would have been cool to solve this problem by constructing a graph from the memory region (non-
corrupted memory spaces are vertices, and adjacent vertices are connected by edges) and keeping
track of its connected components as you remove vertices. But it's actually really easy to do a
manual binary search (done by modifying the value of guess) supplemented by an automated linear
search.
"""

guess = 2048 + 512 + 256 + 128 + 32 + 16 + 1
for corrupted_bytes in range(guess, len(corruption)):
    steps, interior, frontier = 0, set(), {(0, 0)}
    while (size - 1, size - 1) not in frontier and len(frontier) > 0:
        next_frontier = set()
        while len(frontier) > 0:
            x, y = frontier.pop()
            for X, Y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                interior.add((x, y))
                if X >= 0 and Y >= 0 and X < size and Y < size and (X, Y) not in interior and not np.equal(corruption[: corrupted_bytes], (X, Y)).all(1).any():
                    next_frontier.add((X, Y))
        frontier = next_frontier
        steps += 1
    if (size - 1, size - 1) not in frontier:
        break

if corrupted_bytes == guess:
    print("You should lower guess and try again.")
else:
    print(f"Answer to part 2 = {corruption[corrupted_bytes - 1][0]},{corruption[corrupted_bytes - 1][1]}")
