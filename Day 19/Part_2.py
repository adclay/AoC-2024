from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

# towels = ex_towels
# designs = ex_designs

""" -----------------------------------------------------------------------------------------------|
|                 Trim the number of towels used to check if a design is possible                  |
|----------------------------------------------------------------------------------------------- """

short_towels = towels[:]
long_towels = []

def is_possible(design, towels = short_towels, offset = 0):
    if offset >= len(design):
        return True
    for towel in towels:
        if len(towel) <= len(design) and design.startswith(towel, offset) and is_possible(design, towels, offset + len(towel)):
            return True
    return False

for i in range(len(towels) - 1, -1, -1):
    sub_sub_towels = short_towels[:]
    towel = sub_sub_towels.pop(i)
    if is_possible(towel, sub_sub_towels):
        long_towels.append(short_towels.pop(i))

""" -----------------------------------------------------------------------------------------------|
|                  Count how many designs are possible using original towel list                   |
|----------------------------------------------------------------------------------------------- """

def get_decompositions(design, long_history, short_history, offset = 0):
    if offset >= len(design):
        long_history.add(tuple(short_history))
    else:
        for towel in short_towels:
            if len(towel) <= len(design) and design.startswith(towel, offset):
                get_decompositions(design, long_history, short_history + [towel], offset + len(towel))
    return long_history

long_towel_decompositions = [get_decompositions(towel, set(), []) for towel in long_towels]

# This function is supposed to be given a decomposition of a design using the short_towels, and it should return a set of all the decompositions that can be made by combining adjacent towels into long_towels
# It takes too long, so I need to go back to the drawing board and find a new approach
def foo(decomposition, decompositions):
    decompositions.add(decomposition)
    for i in range(len(long_towels)):
        for long_towel_decomposition in long_towel_decompositions[i]:
            for j in range(len(decomposition) - len(long_towel_decomposition) + 1):
                if long_towel_decomposition == decomposition[j : j + len(long_towel_decomposition)]:
                    new_decomposition = tuple(decomposition[i] if i < j else ("".join(long_towel_decomposition) if i == j else decomposition[i + len(long_towel_decomposition) - 1]) for i in range(len(decomposition) - len(long_towel_decomposition) + 1))
                    if new_decomposition not in decompositions:
                        foo(new_decomposition, decompositions)
    return decompositions

design = designs[0]
print(f"design = {design}")
decomp = get_decompositions(designs[0], set(), [], 0).pop()
print(f"decomp = {decomp}")
foo = foo(decomp, set())
print(f"foo = {foo}")



# possible_designs = 0
# for design in designs:
#     if is_possible(design):
#         bases = get_decompositions(design, set(), [], 0)
#         for base in bases:
#             if 
#             # print(base)
#             # print()
# print("Answer to part 2 =", possible_designs)
