from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

antinodes, frequencies = set(), np.unique(grid[grid != '.'])
for freq in frequencies:
    antennas = np.argwhere(grid == freq)
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            pos, step = tuple(antennas[i]), 0
            while pos[0] >= 0 and pos[1] >= 0 and pos[0] < grid.shape[0] and pos[1] < grid.shape[1]:
                antinodes.add(pos)
                step += 1
                pos = tuple(antennas[i] + step * (antennas[j] - antennas[i]))
            pos, step = tuple(2 * antennas[i] - antennas[j]), -1
            while pos[0] >= 0 and pos[1] >= 0 and pos[0] < grid.shape[0] and pos[1] < grid.shape[1]:
                antinodes.add(pos)
                step -= 1
                pos = tuple(antennas[i] + step * (antennas[j] - antennas[i]))
print("Answer to part 2 =", len(antinodes))
