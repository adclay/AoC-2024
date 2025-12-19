from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

steps, interior, frontier = 0, set(), {(0, 0)}
while (size - 1, size - 1) not in frontier:
    next_frontier = set()
    while len(frontier) > 0:
        x, y = frontier.pop()
        for X, Y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            interior.add((x, y))
            if X >= 0 and Y >= 0 and X < size and Y < size and (X, Y) not in interior and not np.equal(corruption[: 1024], (X, Y)).all(1).any():
                next_frontier.add((X, Y))
    frontier = next_frontier
    steps += 1
print("Answer to part 1 =", steps)
