from Puzzle_Input import *

codes = ['456A'] #ex_codes

"""
456A

<<^^A>A>AvvA
<<vAA>^AA>AvA^AvA^A<vAA>^A
<<vAA>A>^AAvA<^A>AAvA^A<vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A

v<<A : v<A<AA>>^A
<<vA : v<<AA>A>^A

(-2,-2),(0,1),(0,1),(2,0)
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
    print("Dict:")
    for key, val in d.items():
        print(f"{key}")
        for sequence in val:
            print(f"\t{sequence}")
    print()

expand = [{
    (-1,-1) : {('<', 0, ( 0,-1),( 1,-1)),         ('^', 0, ( 1,-2),(-1, 1))}, # ^<,  <^
    (-1, 0) : {('^', 0, ( 0,-1))},                                            # ^
    (-1, 1) : {('>', 0, ( 0,-1),( 1, 1)),         ('^', 0, ( 1, 0),(-1,-1))}, # ^>,  >^
    (-1, 2) : {('>', 0, ( 1, 0),(-1,-1),( 1, 1)), ('^', 1, ( 1, 0),(-1,-1))}, # >^>, >>^

    ( 0,-2) : {('<', 1, ( 1,-2))}, # <<
    ( 0,-1) : {('<', 0, ( 1,-2))}, # <
    ( 0, 1) : {('>', 0, ( 1, 0))}, # >
    ( 0, 2) : {('>', 1, ( 1, 0))}, # >>

    ( 1,-2) : {('<', 1, ( 1,-1),( 0,-1)), ('<', 0, ( 1,-2),( 0, 1),( 0,-1))}, # v<<, <v<
    ( 1,-1) : {('<', 0, ( 1,-1),( 0,-1)), ('v', 0, ( 1,-2),( 0, 1))},         # v<,  <v
    ( 1, 0) : {('v', 0, ( 1,-1))},                                            # v
    ( 1, 1) : {('>', 0, ( 1,-1),( 0, 1)), ('v', 0, ( 1, 0),( 0,-1))},         # v>,  >v
}]

for number_of_expansions in range(4):
    print_dict(expand[-1])
    for key, val in expand[-1].items():
        lengths = {}
        for x in val:
            y = len(x) - 2 + x[1]
            if y in lengths:
                lengths[y] += 1
            else:
                lengths[y] = 1
        print(f"{key} - ", end = "")
        keys = list(lengths.keys())
        keys.sort()
        for k in keys:
            print(f"{k}:{lengths[k]}, ", end = "")
        print("}")
    print(f"number_of_expansions = {number_of_expansions}")

    expand.append({})
    for delta in expand[-2].keys():
        expand[-1][delta] = set()
        for sequence in expand[-2][delta]:
            new_sequences = {('A', 0)}
            for new_delta in sequence[2:]:
                new_new_sequences = set()
                for x in new_sequences:
                    y_end, x_end = dirpad[x[0]]
                    for y in expand[-2][new_delta]:
                        if y[2][0] == y_end and y[2][1] + 2 == x_end:
                            new_new_sequences.add((y[0], x[1] + y[1] + 1) + x[2:] + y[3:])
                        else:
                            new_new_sequences.add((y[0], x[1] + y[1]) + x[2:] + ((y[2][0] - y_end, y[2][1] + 2 - x_end),) + y[3:])
                new_sequences = new_new_sequences
            expand[-1][delta] |= new_sequences
        # lengths = {len(x) - 2 + x[1] for x in expand[-1][delta]}
        # expand[-1][delta] = {x for x in expand[-1][delta] if len(x) - 2 + x[1] < min(lengths) + 5}

print(f"Done!")
print_dict(expand[-1])
