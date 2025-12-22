from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

"""
Once you've started a partial towel arrangement for a design, the number of ways to finish the
arrangement depends only on the length of what's left in the design (the suffix). This code works by
keeping track of how many partial towel arrangements with each suffix length there are, starting
with a single partial arrangement of zero towels which has suffix length len(design).
"""

def count_ways(design):
    suffixes = [0 if i != len(design) else 1 for i in range(len(design) + 1)]
    for length in range(len(design), 0, -1):
        for towel in towels:
            if len(towel) <= length and design.startswith(towel, len(design) - length):
                suffixes[length - len(towel)] += suffixes[length]
    return suffixes[0]

possible_ways = 0
for design in designs:
    possible_ways += count_ways(design)
print("Answer to part 2 =", possible_ways)
