from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

pos = np.array(np.where(warehouse == '@')).reshape((2,))
for move in moves:
    if move == '^':
        direction = np.array([-1, 0])
    elif move == '<':
        direction = np.array([0, -1])
    elif move == 'v':
        direction = np.array([1, 0])
    else:
        direction = np.array([0, 1])
    next_move = direction.copy()
    
    while warehouse[tuple(pos + next_move)] != '.':
        if warehouse[tuple(pos + next_move)] == '#':
            break
        next_move += direction

    if warehouse[tuple(pos + next_move)] == '.':
        warehouse[tuple(pos + next_move)] = 'O'
        warehouse[tuple(pos + direction)], warehouse[tuple(pos)] = '@', '.'
        pos += direction

GPS = 0
for y in range(warehouse.shape[0]):
    for x in range(warehouse.shape[1]):
        if warehouse[y, x] == 'O':
            GPS += 100 * y + x
print("Answer to part 1 =", GPS)
