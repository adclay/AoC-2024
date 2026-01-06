from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

price = 0
for secret in secret_numbers:
    for i in range(2000):
        secret = (secret ^ (secret <<  6)) % 16777216
        secret = (secret ^ (secret >>  5)) % 16777216
        secret = (secret ^ (secret << 11)) % 16777216
    price += secret
print("Answer to part 1 =", price)
