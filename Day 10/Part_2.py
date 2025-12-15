from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

rating, trailheads = 0, np.where(topo == 0)
trailheads = np.array([[trailheads[0][i], trailheads[1][i]] for i in range(len(trailheads[0]))])
for trailhead in trailheads:
    locations, next_locations = {tuple(trailhead) : 1}, {}
    for elev in range(1, 10):
        while len(locations) > 0:
            loc = list(locations)[0]
            num = locations.pop(list(locations)[0])
            if loc[0] > 0 and topo[loc[0] - 1, loc[1]] == elev:
                if (loc[0] - 1, loc[1]) in next_locations:
                    next_locations[(loc[0] - 1, loc[1])] += num
                else:
                    next_locations[(loc[0] - 1, loc[1])] = num
            if loc[0] < topo.shape[0] - 1 and topo[loc[0] + 1, loc[1]] == elev:
                if (loc[0] + 1, loc[1]) in next_locations:
                    next_locations[(loc[0] + 1, loc[1])] += num
                else:
                    next_locations[(loc[0] + 1, loc[1])] = num
            if loc[1] > 0 and topo[loc[0], loc[1] - 1] == elev:
                if (loc[0], loc[1] - 1) in next_locations:
                    next_locations[(loc[0], loc[1] - 1)] += num
                else:
                    next_locations[(loc[0], loc[1] - 1)] = num
            if loc[1] < topo.shape[1] - 1 and topo[loc[0], loc[1] + 1] == elev:
                if (loc[0], loc[1] + 1) in next_locations:
                    next_locations[(loc[0], loc[1] + 1)] += num
                else:
                    next_locations[(loc[0], loc[1] + 1)] = num
        locations, next_locations = next_locations, locations
    rating += sum(locations.values())
print("Answer to part 2 =", rating)
