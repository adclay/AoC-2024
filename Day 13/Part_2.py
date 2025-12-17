from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

tokens = 0
for i in range(len(xList)):
    X, Y = xList[i], yList[i]
    X[2] += 10000000000000
    Y[2] += 10000000000000

    # a * X[0] + b * X[1] = X[2]
    # a * Y[0] + b * Y[1] = Y[2]

    det = X[0] * Y[1] - X[1] * Y[0]
    a = Y[1] * X[2] - X[1] * Y[2]
    b = X[0] * Y[2] - Y[0] * X[2]
    if det < 0:
        det, a, b = -det, -a, -b
    if not (a < 0 or b < 0 or a % det or b % det):
        tokens += (3 * a + b) // det
print("Answer to part 2 =", tokens)
