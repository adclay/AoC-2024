from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|               Part 1 - Find time from each position in racetrack to start and end                |
|----------------------------------------------------------------------------------------------- """

start = tuple(np.array(np.where(racetrack == 'S')).reshape((2,)))
end = tuple(np.array(np.where(racetrack == 'E')).reshape((2,)))

# Create graph
graph, cheats = {}, set()
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

            # Cheats
            if y >= 2 and racetrack[y - 2, x] != '#':
                cheats.add((y - 2, x, y, x))
            if x >= 2 and racetrack[y, x - 2] != '#':
                cheats.add((y, x - 2, y, x))

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
|                            Part 1 - Find time savings for each cheat                             |
|----------------------------------------------------------------------------------------------- """

cost, best_cheats = cost_from_start[end], 0
for x0, y0, x1, y1 in cheats:
    if cost - 100 >= cost_from_start[(x0, y0)] + 2 + cost_to_end[(x1, y1)]:
        best_cheats += 1
    if cost - 100 >= cost_from_start[(x1, y1)] + 2 + cost_to_end[(x0, y0)]:
        best_cheats += 1
print("Answer to part 1 =", best_cheats)
