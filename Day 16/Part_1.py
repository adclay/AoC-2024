from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
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

# Dijkstra
unvisited = {vertex : np.iinfo(int).max for vertex in digraph.keys()}
unvisited[(maze.shape[0] - 2, 1, 'E')] = 0
while True:
    vertex = min(unvisited, key = unvisited.get)
    if vertex[0] == 1 and vertex[1] == maze.shape[1] - 2:
        print("Answer to part 1 =", unvisited[vertex])
        break
    for neighbor, weight in digraph[vertex]:
        if neighbor in unvisited:
            distance = unvisited[vertex] + weight
            if distance < unvisited[neighbor]:
                unvisited[neighbor] = distance
    del unvisited[vertex]
