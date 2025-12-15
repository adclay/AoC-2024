from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

score, summits = 0, np.where(topo == 9)
summits = np.array([[summits[0][i], summits[1][i]] for i in range(len(summits[0]))])
for summit in summits:
    locations, next_locations = {tuple(summit)}, set()
    for elev in range(8, -1, -1):
        while len(locations) > 0:
            loc = locations.pop()
            if loc[0] > 0 and topo[loc[0] - 1, loc[1]] == elev:
                next_locations.add((loc[0] - 1, loc[1]))
            if loc[0] < topo.shape[0] - 1 and topo[loc[0] + 1, loc[1]] == elev:
                next_locations.add((loc[0] + 1, loc[1]))
            if loc[1] > 0 and topo[loc[0], loc[1] - 1] == elev:
                next_locations.add((loc[0], loc[1] - 1))
            if loc[1] < topo.shape[1] - 1 and topo[loc[0], loc[1] + 1] == elev:
                next_locations.add((loc[0], loc[1] + 1))
        locations, next_locations = next_locations, locations
    score += len(locations)
print("Answer to part 1 =", score)
