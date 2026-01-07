from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

# Get lock and key dimensions
locks, keys = [], []
for LorK in locks_and_keys:
    if LorK[0, 0] == '#':
        locks.append((np.count_nonzero(LorK[1:-1, 0] == '#'), np.count_nonzero(LorK[1:-1, 1] == '#'), np.count_nonzero(LorK[1:-1, 2] == '#'), np.count_nonzero(LorK[1:-1, 3] == '#'), np.count_nonzero(LorK[1:-1, 4] == '#')))
    else:
        keys.append((np.count_nonzero(LorK[1:-1, 0] == '#'), np.count_nonzero(LorK[1:-1, 1] == '#'), np.count_nonzero(LorK[1:-1, 2] == '#'), np.count_nonzero(LorK[1:-1, 3] == '#'), np.count_nonzero(LorK[1:-1, 4] == '#')))

# Get number of pairs that fit together
matches = 0
for lock in locks:
    for key in keys:
        if np.all(np.array(lock) + np.array(key) < np.array([6,6,6,6,6])):
            matches += 1
print("Answer to part 1 =", matches)
