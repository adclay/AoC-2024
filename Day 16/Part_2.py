from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                Part 2 - Find minimum score to get to each position from the start                |
|----------------------------------------------------------------------------------------------- """

# Create a directed graph with vertices representing the positions in the maze and edge costs
# representing the cost to move from one position to another
digraph = {}
for y in range(maze.shape[0]):
    for x in range(maze.shape[1]):
        if maze[y, x] != '#':
            digraph[(y, x, 'N')] = set([((y, x, 'E'), 1000), ((y, x, 'W'), 1000)])
            digraph[(y, x, 'E')] = set([((y, x, 'N'), 1000), ((y, x, 'S'), 1000)])
            digraph[(y, x, 'S')] = set([((y, x, 'E'), 1000), ((y, x, 'W'), 1000)])
            digraph[(y, x, 'W')] = set([((y, x, 'N'), 1000), ((y, x, 'S'), 1000)])
            if maze[y - 1, x] != '#':
                digraph[(y, x, 'N')].add(((y - 1, x, 'N'), 1))
            if maze[y, x + 1] != '#':
                digraph[(y, x, 'E')].add(((y, x + 1, 'E'), 1))
            if maze[y + 1, x] != '#':
                digraph[(y, x, 'S')].add(((y + 1, x, 'S'), 1))
            if maze[y, x - 1] != '#':
                digraph[(y, x, 'W')].add(((y, x - 1, 'W'), 1))

# Dijkstra (start -> somewhere)
unvisited, cost_from_start = {vertex : np.iinfo(int).max for vertex in digraph.keys()}, {}
unvisited[(maze.shape[0] - 2, 1, 'E')] = 0
while len(unvisited) > 0:
    vertex = min(unvisited, key = unvisited.get)
    for neighbor, weight in digraph[vertex]:
        if neighbor in unvisited:
            distance = unvisited[vertex] + weight
            if distance < unvisited[neighbor]:
                unvisited[neighbor] = distance
    cost_from_start[vertex] = unvisited[vertex]
    del unvisited[vertex]

""" -----------------------------------------------------------------------------------------------|
|                   Part 2 - Find minimum score to get to end from each position                   |
|----------------------------------------------------------------------------------------------- """

# Create a directed graph with vertices representing the positions in the maze and edge costs
# representing the cost to move from one position to another **backwards**
digraph = {}
for y in range(maze.shape[0]):
    for x in range(maze.shape[1]):
        if maze[y, x] != '#':
            digraph[(y, x, 'N')] = set([((y, x, 'E'), 1000), ((y, x, 'W'), 1000)])
            digraph[(y, x, 'E')] = set([((y, x, 'N'), 1000), ((y, x, 'S'), 1000)])
            digraph[(y, x, 'S')] = set([((y, x, 'E'), 1000), ((y, x, 'W'), 1000)])
            digraph[(y, x, 'W')] = set([((y, x, 'N'), 1000), ((y, x, 'S'), 1000)])
            if maze[y - 1, x] != '#':
                digraph[(y, x, 'S')].add(((y - 1, x, 'S'), 1))
            if maze[y, x + 1] != '#':
                digraph[(y, x, 'W')].add(((y, x + 1, 'W'), 1))
            if maze[y + 1, x] != '#':
                digraph[(y, x, 'N')].add(((y + 1, x, 'N'), 1))
            if maze[y, x - 1] != '#':
                digraph[(y, x, 'E')].add(((y, x - 1, 'E'), 1))

# Dijkstra (somewhere -> end)
unvisited, cost_to_end = {vertex : np.iinfo(int).max for vertex in digraph.keys()}, {}
for facing in 'NESW':
    unvisited[(1, maze.shape[1] - 2, facing)] = 0
while len(unvisited) > 0:
    vertex = min(unvisited, key = unvisited.get)
    for neighbor, weight in digraph[vertex]:
        if neighbor in unvisited:
            distance = unvisited[vertex] + weight
            if distance < unvisited[neighbor]:
                unvisited[neighbor] = distance
    cost_to_end[vertex] = unvisited[vertex]
    del unvisited[vertex]

""" -----------------------------------------------------------------------------------------------|
|                                 Part 2 - Find good spots to sit                                  |
|----------------------------------------------------------------------------------------------- """

good_spots_to_sit, min_score = 0, min([cost_from_start[(1, maze.shape[1] - 2, facing)] for facing in 'NESW'])
for y in range(maze.shape[0]):
    for x in range(maze.shape[1]):
        if maze[y, x] != '#':
            for facing in 'NESW':
                if cost_from_start[(y, x, facing)] + cost_to_end[(y, x, facing)] == min_score:
                    good_spots_to_sit += 1
                    break
print("Answer to part 2 =", good_spots_to_sit)
