from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

print("Answer to part 1 = ", end = "")

pointer, first_output = 0, True
while pointer < len(program) - 1:
    opcode, operand, pointer = program[pointer], program[pointer + 1], pointer + 2
    if opcode in [0, 2, 5, 6, 7]:
        if operand == 4:
            operand = registers[0]
        elif operand == 5:
            operand = registers[1]
        elif operand == 6:
            operand = registers[2]
        elif operand == 7:
            print("INVALID INSTRUCTION")

    if opcode == 0:
        registers[0] >>= operand
    elif opcode == 1:
        registers[1] ^= operand
    elif opcode == 2:
        registers[1] = operand % 8
    elif opcode == 3:
        if registers[0]:
            pointer = operand
    elif opcode == 4:
        registers[1] ^= registers[2]
    elif opcode == 5:
        if first_output:
            print(f"{operand % 8}", end = "")
            first_output = False
        else:
            print(f",{operand % 8}", end = "")
    elif opcode == 6:
        registers[1] = registers[0] >> operand
    elif opcode == 7:
        registers[2] = registers[0] >> operand
print()
