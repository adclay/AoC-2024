from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

checksum, position = 0, 0
left_id, right_id = 0, (len(disk) - 1) // 2
left_size, right_size = ord(disk[0]) - ord('0'), ord(disk[2 * right_id]) - ord('0')
while True:
    # Block of memory that stays in place
    while left_size > 0:
        checksum += left_id * position
        position += 1
        left_size -= 1
    left_id += 1
    if left_id == right_id:
        left_size = right_size
        break
    left_size = ord(disk[2 * left_id]) - ord('0')

    # Block of memory that needs to be filled
    gap_size = ord(disk[2 * left_id - 1]) - ord('0')
    while gap_size > 0:
        if right_size == 0:
            right_id -= 1
            if right_id == left_id:
                right_size = left_size
                break
            right_size = ord(disk[2 * right_id]) - ord('0')
        while gap_size > 0 and right_size > 0:
            checksum += right_id * position
            position += 1
            gap_size -= 1
            right_size -= 1
    if right_id == left_id:
        break
for i in range(left_size):
    checksum += left_id * position
    position += 1
print("Answer to part 1 =", checksum)
