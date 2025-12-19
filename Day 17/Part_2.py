from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

"""
Program:
    2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0
Pseudocode:
    0: B = A % 8
    1: B = B ^ 5
    2: C = A >> B
    3: B = B ^ C
    4: B = B ^ 6
    5: A = A >> 3
    6: output B % 8
    7: HALT if A == 0 else goto 0
Optimized pseudocode:
    0: output ((A >> ((A & 7) ^ 5)) ^ A ^ 3) & 7
    1: A = A >> 3
    2: HALT if A == 0 else goto 0
Observations:
    The output of one run through the code depends upon only the bottom 10 bits of A. We can find
    all the 10-bit (dectit) inputs that yield each 8-bit (octit) output. Then we can recursively
    construct A such that A >> 3 is always compatible with the input required for the next run.
"""

# Find dectits that output the correct octits
possible_dectits = []
for octit in program:
    possible_dectits.append(set())
    for dectit in range(1 << 10):
        if octit == ((dectit >> ((dectit & 7) ^ 5)) ^ dectit ^ 3) & 7:
            possible_dectits[-1].add(dectit)

# Construct possible values of register A
A = {0}
for dectits in possible_dectits[:: -1]:
    new_A = set()
    for dectit in dectits:
        for a in A:
            if (a & 127) == (dectit >> 3):
                new_A.add((a << 3) | (dectit & 7))
    A = new_A
print("Answer to part 2 =", min(A))
