from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|       Part 2 - Find time from each position in racetrack to start and end (same as part 1)       |
|----------------------------------------------------------------------------------------------- """

start = tuple(np.array(np.where(racetrack == 'S')).reshape((2,)))
end = tuple(np.array(np.where(racetrack == 'E')).reshape((2,)))

# Create graph
graph = {}
for y in range(racetrack.shape[0]):
    for x in range(racetrack.shape[1]):
        if racetrack[y, x] != '#':
            # Not cheats
            edges = set()
            if racetrack[y - 1, x] != '#':
                edges.add((y - 1, x))
            if racetrack[y, x + 1] != '#':
                edges.add((y, x + 1))
            if racetrack[y + 1, x] != '#':
                edges.add((y + 1, x))
            if racetrack[y, x - 1] != '#':
                edges.add((y, x - 1))
            if len(edges) > 0:
                graph[(y, x)] = edges

# Dijkstra (start -> ?)
unvisited, cost_from_start = {vertex : np.iinfo(int).max for vertex in graph.keys()}, {}
unvisited[start] = 0
while len(unvisited) > 0:
    vertex = min(unvisited, key = unvisited.get)
    for neighbor in graph[vertex]:
        if neighbor in unvisited:
            distance = unvisited[vertex] + 1
            if distance < unvisited[neighbor]:
                unvisited[neighbor] = distance
    cost_from_start[vertex] = unvisited[vertex]
    del unvisited[vertex]
    
# Dijkstra (? -> end)
unvisited, cost_to_end = {vertex : np.iinfo(int).max for vertex in graph.keys()}, {}
unvisited[end] = 0
while len(unvisited) > 0:
    vertex = min(unvisited, key = unvisited.get)
    for neighbor in graph[vertex]:
        if neighbor in unvisited:
            distance = unvisited[vertex] + 1
            if distance < unvisited[neighbor]:
                unvisited[neighbor] = distance
    cost_to_end[vertex] = unvisited[vertex]
    del unvisited[vertex]

""" -----------------------------------------------------------------------------------------------|
|                                   Part 2 - Iterate over cheats                                   |
|----------------------------------------------------------------------------------------------- """

cost, best_cheats = cost_from_start[end], 0
for y in range(racetrack.shape[0]):
    for x in range(racetrack.shape[1]):
        if racetrack[y, x] != '#':
            for y_delta in range(max(-20, -y), min(21, racetrack.shape[0] - y)):
                for x_delta in range(max(-(20 - abs(y_delta)), -x), min(20 - abs(y_delta) + 1, racetrack.shape[1] - x)):
                    if racetrack[y + y_delta, x + x_delta] != '#':
                        if cost - 100 >= cost_from_start[(y, x)] + abs(y_delta) + abs(x_delta) + cost_to_end[(y + y_delta, x + x_delta)]:
                            best_cheats += 1
print("Answer to part 2 =", best_cheats)
