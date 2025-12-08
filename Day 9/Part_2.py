from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

disk = np.array(list(disk + "0"), dtype = int).reshape(((len(disk) + 1) // 2, 2))
disk = np.insert(disk, [0], [[x] for x in range(disk.shape[0])], axis = 1)

for ID in range(disk[-1, 0], 0, -1):
    index = np.argwhere(disk[:, 0] == ID)[0, 0]
    spaces = np.argwhere(disk[: index, -1] >= disk[index, 1])
    if len(spaces) == 0:
        continue
    
    new_index = spaces[0, 0]
    disk[index - 1, 2] += disk[index, 1] + disk[index, 2]
    disk[index, 2] = disk[new_index, 2] - disk[index, 1]
    disk[new_index, 2] = 0
    disk = np.insert(disk, new_index + 1, disk[index], axis = 0)
    disk = np.delete(disk, index + 1, axis = 0)

checksum, position = 0, 0
for file in disk:
    checksum += file[0] * (file[1] * position + file[1] * (file[1] - 1) // 2)
    position += file[1] + file[2]
print("Answer to part 2 =", checksum)
