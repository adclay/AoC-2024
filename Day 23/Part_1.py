from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

# Create graph using vertex set and edge set
vertices, edges = set(), set()
for edge in network:
    u, v = edge[:2], edge[3:]
    if u > v:
        u, v = v, u

    vertices.add(u)
    vertices.add(v)
    edges.add((u, v))

# Sort vertices alphabetically
vertices = list(vertices)
vertices.sort()
n = len(vertices)

# Find triangles
triangles = 0
for i in range(n - 2):
    vi = vertices[i]
    for j in range(i + 1, n - 1):
        vj = vertices[j]
        for k in range(j + 1, n):
            vk = vertices[k]
            if (vi[0] == 't' or vj[0] == 't' or vk[0] == 't') and (vi, vj) in edges and (vi, vk) in edges and (vj, vk) in edges:
                triangles += 1
print("Answer to part 1 =", triangles)
