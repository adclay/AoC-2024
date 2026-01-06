from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

M = np.array([
    [0,0, 1,0,1, 0,0,0,0, 0,0,0,0], #  ^A : <A>A
    [0,1, 0,0,0, 0,0,0,0, 0,0,0,0], #   A : A

    [0,2, 0,0,0, 0,0,0,0, 0,1,1,0], #  <A : v<<A>>^A
    [0,0, 0,0,0, 0,1,1,0, 0,0,0,0], #  vA : <vA^>A
    [1,0, 0,1,0, 0,0,0,0, 0,0,0,0], #  >A : vA^A

    # Preferred
    [0,1, 0,0,1, 0,0,0,0, 0,1,1,0], # <^A : v<<A>^A>A
    [1,0, 1,0,0, 0,0,0,1, 0,0,0,0], # ^>A : <Av>A^A
    [0,1, 0,0,1, 0,1,0,0, 0,0,1,0], # <vA : v<<A>A^>A
    [1,0, 0,0,1, 0,0,1,0, 0,0,0,0], # v>A : <vA>A^A

    # Not preferred
    [0,1, 1,0,0, 0,0,0,0, 0,1,1,0], # ^<A : <Av<A>>^A
    [0,0, 0,1,1, 1,0,0,0, 0,0,0,0], # >^A : vA<^A>A
    [0,1, 1,0,0, 0,0,1,0, 0,1,0,0], # v<A : <vA<A>>^A
    [0,0, 1,1,0, 0,1,0,0, 0,0,0,0]  # >vA : vA<A^>A
], dtype = int)

""" -----------------------------------------------------------------------------------------------|
|                       Part 2 - Convert numpad code into second dirpad code                       |
|----------------------------------------------------------------------------------------------- """

dpad_codes = []
for code in codes:
    dpad_keys = np.zeros((1,13), dtype = int)
    y, x = numpad['A']

    for key in code:
        new_y, new_x = numpad[key]

        if new_y < y and new_x == x: # ^
            dpad_keys[0] += M[0]
            dpad_keys[0, 1] += y - new_y - 1
        elif new_y == y and new_x == x: # A
            dpad_keys[0, 1] += 1

        elif new_y == y and new_x < x: # <
            dpad_keys[0] += M[2]
            dpad_keys[0, 1] += x - new_x - 1
        elif new_y > y and new_x == x: # v
            dpad_keys[0] += M[3]
            dpad_keys[0, 1] += new_y - y - 1
        elif new_y == y and new_x > x: # >
            dpad_keys[0] += M[4]
            dpad_keys[0, 1] += new_x - x - 1

        elif new_y < y and new_x < x: # ^<
            if y == 3 and new_x == 0:
                dpad_keys[0] += M[9]
            else:
                dpad_keys[0] += M[5]
            dpad_keys[0, 1] += (y - new_y) + (x - new_x) - 2

        elif new_y < y and new_x > x: # ^>
            dpad_keys[0] += M[6]
            dpad_keys[0, 1] += (y - new_y) + (new_x - x) - 2
        elif new_y > y and new_x < x: # v<
            dpad_keys[0] += M[7]
            dpad_keys[0, 1] += (new_y - y) + (x - new_x) - 2

        elif new_y > y and new_x > x: # v>
            if new_y == 3 and x == 0:
                dpad_keys[0] += M[12]
            else:
                dpad_keys[0] += M[8]
            dpad_keys[0, 1] += (new_y - y) + (new_x - x) - 2

        y, x = new_y, new_x

    dpad_codes.append(dpad_keys)

""" -----------------------------------------------------------------------------------------------|
|                     Part 2 - Convert second dirpad code into my dirpad code                      |
|----------------------------------------------------------------------------------------------- """

for number_of_dpads in range(24):
    for i in range(len(codes)):
        dpad_codes[i] = dpad_codes[i] @ M

""" -----------------------------------------------------------------------------------------------|
|                                  Part 2 - Calculate complexity                                   |
|----------------------------------------------------------------------------------------------- """

complexity = 0
for i in range(len(codes)):
    length = np.dot(dpad_codes[i].flatten(), [2,1, 2,2,2, 3,3,3,3, 3,3,3,3])
    numeric = int(codes[i][:-1])
    print(f"{codes[i]}: {length} * {numeric}")
    complexity += length * numeric
print("Answer to part 2 =", complexity)
