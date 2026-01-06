from Puzzle_Input import *

# codes = ex_codes #['456A']

"""
456A

<<^^A>A>AvvA
<<vAA>^AA>AvA^AvA^A<vAA>^A
<<vAA>A>^AAvA<^A>AAvA^A<vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A

v<<A : v<A<AA>>^A
<<vA : v<<AA>A>^A

(-2,-2),(0,1),(0,1),(2,0)

029A
<A^A^^>AvvvA
v<>^><><>v^<v>^

('^', 4, (1, -1), (0, -1), (0, 2), (-1, -1), (1, 1), (0, -2), (0, 2), (0, -2), (0, 2), (0, -1), (-1, 0), (1, -1), (0, 1), (0, 1), (-1, -1))
"""

""" -----------------------------------------------------------------------------------------------|
|                                             Attempt                                              |
|----------------------------------------------------------------------------------------------- """

"""
We're going to convert the key presses into a sequence of tuples which represent how far the robots
have to move. For example, to press '456A', we would do this:
    (-2,-2),(0,1),(0,1),(2,0)
where the first entry of each tuple represents the change in y-position, and the second entry
represents the change in x-position.

The directional keypad instructions will always be a  of tuples of the form (dy,dx) where
    -1 <= dy <= 1   and   -2 <= dx <= 2.
We're going to find the most efficient ways of performing these types of moves by finding all the
ways to perform them as we double the number of directional keypad robots. Then we'll find the most
efficient ways to do them after 25 iterations, and we'll see how efficiently we can do the numeric
keypad moves.

base_expansion[k][i] = {expansions of ['<','v','>','^'][i] after 2^k iterations}
"""

def print_dict(d):
    # # Dict
    # print("Dict:")
    # for key, val in d.items():
    #     print(f"{key}")
    #     for sequence in val:
    #         print(f"\t{sequence}")

    # Length
    for key, val in d.items():
        lengths = {}
        for x in val:
            y = len(x) - 1 + x[0]
            if y in lengths:
                lengths[y] += 1
            else:
                lengths[y] = 1
        print(f"{key} - ", end = "{ ")
        keys = list(lengths.keys())
        keys.sort()
        for k in keys:
            print(f"{k}:{lengths[k]}, ", end = "")
        print("}")

    # Newline
    print()

""" -----------------------------------------------------------------------------------------------|
|                    Part 2 - Find minimum length expansions of each arrow key                     |
|----------------------------------------------------------------------------------------------- """

"""
(-1,-1)
(-1, 0)
(-1, 1)
(-1, 2)

( 0,-2)
( 0,-1)
( 0, 0)
( 0, 1)
( 0, 2)

( 1,-2)
( 1,-1)
( 1, 0)
( 1, 1)
"""

expand = [[
    {(0,0,0,1, 0,1,0,0,0, 0,1,0,0), (0,0,1,0, 0,0,0,1,0, 1,0,0,0)}, # ^<,  <^
    {(0,0,0,0, 0,1,0,1,0, 0,0,0,0)                               }, # ^
    {(0,1,0,0, 0,1,0,0,0, 0,0,0,1), (1,0,0,0, 0,0,0,1,0, 0,0,1,0)}, # ^>,  >^
    {(1,1,0,0, 0,0,0,0,0, 0,0,1,1), (1,0,0,0, 0,0,1,1,0, 0,0,1,0)}, # >^>, >>^

    {(0,0,0,1, 0,0,1,0,0, 1,0,0,0)}, # <<
    {(0,0,0,1, 0,0,0,0,0, 1,0,0,0)}, # <
    {(0,0,0,0, 0,0,1,0,0, 0,0,0,0)}, # A
    {(0,1,0,0, 0,0,0,0,0, 0,0,1,0)}, # >
    {(0,1,0,0, 0,0,1,0,0, 0,0,1,0)}, # >>

    {(0,0,0,1, 0,1,1,0,0, 0,1,0,0), (0,0,0,1, 0,1,0,1,0, 1,0,0,0)}, # v<<, <v<
    {(0,0,0,1, 0,1,0,0,0, 0,1,0,0), (0,0,1,0, 0,0,0,1,0, 1,0,0,0)}, # v<,  <v
    {(0,0,1,0, 0,0,0,0,0, 0,1,0,0)                               }, # v
    {(0,1,0,0, 0,0,0,1,0, 0,1,0,0), (0,0,1,0, 0,1,0,0,0, 0,0,1,0)}  # v>,  >v
]]

for number_of_dirpad_robots in range(1):
    print(number_of_dirpad_robots)

    expand.append([set() for x in range(13)])
    for i in range(13):
        for vec in expand[-2][i]:
            val = {(0,0,0,0, 0,0,0,0,0, 0,0,0,0)}
            for j in range(13):
                val = {tuple(np.array(x) + vec[j] * np.array(y)) for x in val for y in expand[0][j]}
            expand[-1][i] |= val
        min_length = min({sum(x) for x in expand[-1][i]})
        expand[-1][i] = {x for x in expand[-1][i] if sum(x) == min_length}

for i in range(len(expand)):
    for j in range(len(expand[0])):
        expand[i][j] = int(min({sum(x) for x in expand[i][j]}))

""" -----------------------------------------------------------------------------------------------|
|                    Part 2 - Find minimum length expansions of each arrow key                     |
|----------------------------------------------------------------------------------------------- """

# expand = [{
#     (-1,-1) : {(0, ( 0,-1),( 1,-1),(-1, 2)),         (0, ( 1,-2),(-1, 1),( 0, 1))}, # ^<,  <^
#     (-1, 0) : {(0, ( 0,-1),( 0, 1))},                                               # ^
#     (-1, 1) : {(0, ( 0,-1),( 1, 1),(-1, 0)),         (0, ( 1, 0),(-1,-1),( 0, 1))}, # ^>,  >^
#     (-1, 2) : {(0, ( 1, 0),(-1,-1),( 1, 1),(-1, 0)), (1, ( 1, 0),(-1,-1),( 0, 1))}, # >^>, >>^

#     ( 0,-2) : {(1, ( 1,-2),(-1, 2))}, # <<
#     ( 0,-1) : {(0, ( 1,-2),(-1, 2))}, # <
#     ( 0, 1) : {(0, ( 1, 0),(-1, 0))}, # >
#     ( 0, 2) : {(1, ( 1, 0),(-1, 0))}, # >>

#     ( 1,-2) : {(1, ( 1,-1),( 0,-1),(-1, 2)), (0, ( 1,-2),( 0, 1),( 0,-1),(-1, 2))}, # v<<, <v<
#     ( 1,-1) : {(0, ( 1,-1),( 0,-1),(-1, 2)), (0, ( 1,-2),( 0, 1),(-1, 1))},         # v<,  <v
#     ( 1, 0) : {(0, ( 1,-1),(-1, 1))},                                               # v
#     ( 1, 1) : {(0, ( 1,-1),( 0, 1),(-1, 0)), (0, ( 1, 0),( 0,-1),(-1, 1))},         # v>,  >v
# }]

# # Expand expand[i] sequences by plugging in sequences from expand[j]
# def expand_more(i, j):
#     expand.append({})
#     for delta in expand[0].keys():
#         expand[-1][delta] = set()
#         for sequence in expand[i][delta]:
#             new_sequences = {(0,)}
#             for new_delta in sequence[1:]:
#                 new_new_sequences = set()
#                 for x in new_sequences:
#                     for y in expand[j][new_delta]:
#                         new_new_sequences.add((x[0] + y[0],) + x[1:] + y[1:])
#                 new_sequences = new_new_sequences
#             expand[-1][delta] |= new_sequences
#         min_length = min({len(x) - 1 + x[0] for x in expand[-1][delta]})
#         expand[-1][delta] = {x for x in expand[-1][delta] if len(x) - 1 + x[0] == min_length}

# for i in range(4):
#     print(f"number_of_expansions = {1 << i}")
#     print_dict(expand[-1])
#     expand_more(i, i)
# print(f"number_of_expansions = {1 << 4}")
# print_dict(expand[-1])

# expand_more(4, 3)
# print(f"number_of_expansions = {24}")
# print_dict(expand[-1])

# expand_more(5, 0)
# print(f"number_of_expansions = {25}")
# print_dict(expand[-1])

# for i in range(len(expand)):
#     for key in expand[i].keys():
#         expand[i][key] = min({len(x) - 2 + x[1] for x in expand[i][key]})

""" -----------------------------------------------------------------------------------------------|
|                          Part 2 - Convert numpad codes into dpad codes                           |
|----------------------------------------------------------------------------------------------- """

dpad_codes = []
for code in codes:
    dpad = {''}
    y, x = numpad['A']
    for key in code:
        new_y, new_x = numpad[key]
        y_arrows = 'v' * (new_y - y) if new_y > y else '^' * (y - new_y)
        x_arrows = '>' * (new_x - x) if new_x > x else '<' * (x - new_x)

        new_dpad = set()
        if (y < 3 and new_y < 3) or (x > 0 and new_x > 0):
            for command in dpad:
                new_dpad.add(command + y_arrows + x_arrows + 'A')
                new_dpad.add(command + x_arrows + y_arrows + 'A')
        elif x == 0:
            for command in dpad:
                new_dpad.add(command + x_arrows + y_arrows + 'A')
        else:
            for command in dpad:
                new_dpad.add(command + y_arrows + x_arrows + 'A')

        dpad = new_dpad
        y, x = new_y, new_x
    dpad_codes.append(dpad)

for i in range(len(codes)):
    new_code = set()
    for code in dpad_codes[i]:
        dpad = {('A', 0)}
        y, x = dirpad['A']
        for key in code:
            new_y, new_x = dirpad[key]
            new_dpad = set()
            for command in dpad:
                if new_y == y and new_x == x:
                    new_dpad.add((key, command[1] + 1) + command[2:])
                else:
                    new_dpad.add((key, command[1]) + command[2:] + ((new_y - y, new_x - x),))
            dpad = new_dpad
            y, x = new_y, new_x
        new_code |= dpad
    dpad_codes[i] = new_code

""" -----------------------------------------------------------------------------------------------|
|                                  Part 2 - Calculate complexity                                   |
|----------------------------------------------------------------------------------------------- """

# def get_complexity(sequence):
#     complexity = sequence[1]
#     for key in sequence[2:]:
#         complexity += expand[0][key]
#     return complexity

# def get_complexity(sequence):
#     sequences = {('A', sequence[1])}
#     for delta in sequence[2:]:
#         new_sequences = set()
#         for x in sequences:
#             y_end, x_end = dirpad[x[0]]
#             for y in expand[0][delta]:
#                 if y[2][0] == y_end and y[2][1] + 2 == x_end:
#                     new_sequences.add((y[0], x[1] + y[1] + 1) + x[2:] + y[3:])
#                 else:
#                     new_sequences.add((y[0], x[1] + y[1]) + x[2:] + ((y[2][0] - y_end, y[2][1] + 2 - x_end),) + y[3:])
#         sequences = new_sequences

#     print(sequence)
#     for s in sequences:
#         print(f"\t{s}")
#     print()
#     return min({len(x) - 2 + x[1] for x in sequences})

def get_complexity(sequence):
    complexity = sequence[1]
    for delta in sequence[2:]:
        if delta == (-1,-1):
            complexity += expand[-1][0]
        elif delta == (-1, 0):
            complexity += expand[-1][1]
        elif delta == (-1, 1):
            complexity += expand[-1][2]
        elif delta == (-1, 2):
            complexity += expand[-1][3]

        elif delta == ( 0,-2):
            complexity += expand[-1][4]
        elif delta == ( 0,-1):
            complexity += expand[-1][5]
        elif delta == ( 0, 0):
            complexity += expand[-1][6]
        elif delta == ( 0, 1):
            complexity += expand[-1][7]
        elif delta == ( 0, 2):
            complexity += expand[-1][8]

        elif delta == ( 1,-2):
            complexity += expand[-1][9]
        elif delta == ( 1,-1):
            complexity += expand[-1][10]
        elif delta == ( 1, 0):
            complexity += expand[-1][11]
        elif delta == ( 1, 1):
            complexity += expand[-1][12]

        else:
            return -1
    return complexity

complexity = 0
for i in range(len(codes)):
    length = min({get_complexity(x) for x in dpad_codes[i]})
    numeric = int(codes[i][:-1])
    print(f"{codes[i]}: {length} * {numeric}")
    complexity += length * numeric
print("Answer to part 2 =", complexity)
