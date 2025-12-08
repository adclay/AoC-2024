from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

calibration = 0
for eq in eqs:
    for i in range(3 ** (len(eq) - 2)):
        result = eq[1]
        for x in eq[2:]:
            if i % 3 == 0:
                result += x
            elif i % 3 == 1:
                result *= x
            else:
                if x >= 100:
                    result *= 1000
                elif x >= 10:
                    result *= 100
                else:
                    result *= 10
                result += x
            i //= 3
        if result == eq[0]:
            calibration += eq[0]
            break
print("Answer to part 2 =", calibration)
