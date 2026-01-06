from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

"""
Notes:
    The network is 13-regular
    There are no 14-cliques
    There is a 13-clique
"""

# Create graph using {vertex : {neighbors}} dictionary
graph = {}
for edge in network:
    u, v = edge[:2], edge[3:]
    if u in graph:
        graph[u].add(v)
    else:
        graph[u] = {v}
    if v in graph:
        graph[v].add(u)
    else:
        graph[v] = {u}

# Find 13-clique
def count_edges(V):
    edges = 0
    for v in V:
        for u in graph[v]:
            if u in V:
                edges += 1
    return edges // 2
clique = [v for v in graph.keys() if count_edges(graph[v]) == 66]
clique.sort()

# Print answer
print("Answer to part 2 =", clique[0], end = "")
for v in clique[1:]:
    print(f",{v}", end = "")
print()
