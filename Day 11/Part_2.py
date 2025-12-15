from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

def dic_add(dic, key, val):
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val

# Initialize 
line, number_of_stones = {}, len(stones)
for stone in stones:
    line[stone] = 1

# Apply rules
for i in range(75):
    new_line = {}
    for key, val in line.items():
        # Rule 1
        if key == 0:
            dic_add(new_line, 1, val)
            continue
        
        # Rule 2
        num, digits = key, 0
        while num > 0:
            digits += 1
            num //= 10
        if digits % 2 == 0:
            left, right = key // (10 ** (digits // 2)), key % (10 ** (digits // 2))
            dic_add(new_line, left, val)
            dic_add(new_line, right, val)
            number_of_stones += val
            continue
        
        # Rule 3
        dic_add(new_line, key * 2024, val)
    line = new_line
print("Answer to part 2 =", number_of_stones)
