from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

calibration = 0
for eq in eqs:
    for i in range(1 << (len(eq) - 2)):
        result = eq[1]
        for x in eq[2:]:
            if i % 2:
                result += x
            else:
                result *= x
            i //= 2
        if result == eq[0]:
            calibration += eq[0]
            break
print("Answer to part 1 =", calibration)
