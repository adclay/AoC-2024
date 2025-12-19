from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

def is_possible(design, towels = towels, offset = 0):
    if offset >= len(design):
        return True
    for towel in towels:
        if len(towel) <= len(design) and design.startswith(towel, offset) and is_possible(design, towels, offset + len(towel)):
            return True
    return False

# Trim the number of towels we need to use down
for i in range(len(towels) - 1, -1, -1):
    sub_towels = towels[:]
    towel = sub_towels.pop(i)
    if is_possible(towel, sub_towels):
        towels.pop(i)

# Check if designs are possible using this smaller towel list
possible_designs = 0
for design in designs:
    if is_possible(design):
        possible_designs += 1
print("Answer to part 1 =", possible_designs)
