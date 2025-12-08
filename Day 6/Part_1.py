from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

cur_pos, cur_dir = [int(x[0]) for x in np.where(area == '^')], 0
while True:
    area[cur_pos[0], cur_pos[1]] = 'X'
    if cur_dir == 0:
        if cur_pos[0] == 0:
            break
        elif area[cur_pos[0] - 1, cur_pos[1]] == '#':
            cur_dir = 1
        else:
            cur_pos[0] -= 1
    elif cur_dir == 1:
        if cur_pos[1] == area.shape[1] - 1:
            break
        elif area[cur_pos[0], cur_pos[1] + 1] == '#':
            cur_dir = 2
        else:
            cur_pos[1] += 1
    elif cur_dir == 2:
        if cur_pos[0] == area.shape[0] - 1:
            break
        elif area[cur_pos[0] + 1, cur_pos[1]] == '#':
            cur_dir = 3
        else:
            cur_pos[0] += 1
    elif cur_dir == 3:
        if cur_pos[1] == 0:
            break
        elif area[cur_pos[0], cur_pos[1] - 1] == '#':
            cur_dir = 0
        else:
            cur_pos[1] -= 1
print("Answer to part 1 =", len(area[area == 'X']))
