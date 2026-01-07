from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

# Evaluate instructions
while len(instructions) > 0:
    for i in range(len(instructions) - 1, -1, -1):
        instr = instructions[i]
        if instr[0] not in registers or instr[2] not in registers:
            continue

        if instr[1] == 'AND':
            registers[instr[3]] = registers[instr[0]] & registers[instr[2]]
        elif instr[1] == 'OR':
            registers[instr[3]] = registers[instr[0]] | registers[instr[2]]
        elif instr[1] == 'XOR':
            registers[instr[3]] = registers[instr[0]] ^ registers[instr[2]]
        else:
            print("BAD!!!")

        del instructions[i]

# Construct answer
Z = 0
while f"z{Z:02d}" in registers:
    Z += 1
answer = 0
for i in range(Z - 1, -1, -1):
    answer = (answer << 1) + registers[f"z{i:02d}"]
print("Answer to part 1 =", answer)
