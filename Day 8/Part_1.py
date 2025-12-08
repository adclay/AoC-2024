from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

antinodes, frequencies = set(), np.unique(grid[grid != '.'])
for freq in frequencies:
    antennas = np.argwhere(grid == freq)
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            antinodes.add(tuple(2 * antennas[i] - antennas[j]))
            antinodes.add(tuple(2 * antennas[j] - antennas[i]))
print("Answer to part 1 =", len([x for x in antinodes if x[0] >= 0 and x[1] >= 0 and x[0] < grid.shape[0] and x[1] < grid.shape[1]]))
