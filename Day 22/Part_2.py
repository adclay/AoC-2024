from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

price = {(a,b,c,d) : 0 for a in range(-9,10) for b in range(-9,10) for c in range(-9,10) for d in range(-9,10)}

for secret in secret_numbers:
    change = []
    for i in range(4):
        old_secret = secret
        secret = (secret ^ (secret <<  6)) % 16777216
        secret = (secret ^ (secret >>  5)) % 16777216
        secret = (secret ^ (secret << 11)) % 16777216

        change.append(secret % 10 - old_secret % 10)

    found = {tuple(change)}
    price[tuple(change)] += secret % 10

    for i in range(1996):
        old_secret = secret
        secret = (secret ^ (secret <<  6)) % 16777216
        secret = (secret ^ (secret >>  5)) % 16777216
        secret = (secret ^ (secret << 11)) % 16777216

        del change[0]
        change.append(secret % 10 - old_secret % 10)

        if tuple(change) not in found:
            found.add(tuple(change))
            price[tuple(change)] += secret % 10

print("Answer to part 2 =", max(price.values()))
