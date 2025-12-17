from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

# xList = ex_xList
# yList = ex_yList

tokens = 0
for i in range(len(xList)):
    X, Y = xList[i], yList[i]
    for b in range(100, -1, -1):
        x, y = X[2] - b * X[1], Y[2] - b * Y[1]
        if x < 0 or y < 0 or x % X[0] or y % Y[0]:
            continue
        a = x // X[0]
        if a > 100:
            break
        if a == y // Y[0]:
            tokens += 3 * a + b
            break
print("Answer to part 1 =", tokens)
