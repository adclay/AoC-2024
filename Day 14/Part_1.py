from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

quadrants = np.zeros((4,), dtype = int)
for robot in robots:
    position = (robot[:2] + 100 * robot[2:]) % np.array(size)
    if position[0] < size[0] // 2:
        if position[1] < size[1] // 2:
            quadrants[0] += 1
        elif position[1] > size[1] // 2:
            quadrants[1] += 1
    elif position[0] > size[0] // 2:
        if position[1] < size[1] // 2:
            quadrants[2] += 1
        elif position[1] > size[1] // 2:
            quadrants[3] += 1
print("Answer to part 1 =", np.prod(quadrants))
