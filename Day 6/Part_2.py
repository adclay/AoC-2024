from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

def is_loop(guard_pos, guard_dir, obstacle_pos):
    visited = set()
    while (guard_pos[0], guard_pos[1], guard_dir) not in visited:
        visited.add((guard_pos[0], guard_pos[1], guard_dir))

        if guard_dir == 0:
            if guard_pos[0] == 0:
                return False
            elif area[guard_pos[0] - 1, guard_pos[1]] == '#' or (guard_pos[0] - 1, guard_pos[1]) == obstacle_pos:
                guard_dir = 1
            else:
                guard_pos[0] -= 1
        elif guard_dir == 1:
            if guard_pos[1] == area.shape[1] - 1:
                return False
            elif area[guard_pos[0], guard_pos[1] + 1] == '#' or (guard_pos[0], guard_pos[1] + 1) == obstacle_pos:
                guard_dir = 2
            else:
                guard_pos[1] += 1
        elif guard_dir == 2:
            if guard_pos[0] == area.shape[0] - 1:
                return False
            elif area[guard_pos[0] + 1, guard_pos[1]] == '#' or (guard_pos[0] + 1, guard_pos[1]) == obstacle_pos:
                guard_dir = 3
            else:
                guard_pos[0] += 1
        elif guard_dir == 3:
            if guard_pos[1] == 0:
                return False
            elif area[guard_pos[0], guard_pos[1] - 1] == '#' or (guard_pos[0], guard_pos[1] - 1) == obstacle_pos:
                guard_dir = 0
            else:
                guard_pos[1] -= 1
    return True
    
cur_pos, cur_dir = [int(x[0]) for x in np.where(area == '^')], 0
while True:
    if area[cur_pos[0], cur_pos[1]] == '.':
        area[cur_pos[0], cur_pos[1]] = cur_dir

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

good_loop_positions = 0
for obstacle_pos in np.argwhere(area == '0'):
    if is_loop([obstacle_pos[0] + 1, obstacle_pos[1]], 0, (obstacle_pos[0], obstacle_pos[1])):
        good_loop_positions += 1
for obstacle_pos in np.argwhere(area == '1'):
    if is_loop([obstacle_pos[0], obstacle_pos[1] - 1], 1, (obstacle_pos[0], obstacle_pos[1])):
        good_loop_positions += 1
for obstacle_pos in np.argwhere(area == '2'):
    if is_loop([obstacle_pos[0] - 1, obstacle_pos[1]], 2, (obstacle_pos[0], obstacle_pos[1])):
        good_loop_positions += 1
for obstacle_pos in np.argwhere(area == '3'):
    if is_loop([obstacle_pos[0], obstacle_pos[1] + 1], 3, (obstacle_pos[0], obstacle_pos[1])):
        good_loop_positions += 1
print("Answer to part 2 =", good_loop_positions)
