from Puzzle_Input import *

"""
I solved this problem by using the code in the "Check for issues" section to determine which bits
were being set incorrectly. After I chose a bit to try to fix, I printed the instructions used to
set that bit by using the code in the "Print instruction dependencies" section. I manually looked at
the instructions to determine which ones needed to be swapped, and I added the swap in the "Swap
instructions" section. I did this for all four swaps, starting by fixing the bit with the least
significance.
"""

""" -----------------------------------------------------------------------------------------------|
|                                  Part 1 - Wrapped as a function                                  |
|----------------------------------------------------------------------------------------------- """

N = 46

def evaluate(x, y):
    # Initialize registers
    registers = {}
    for i in range(N - 1):
        registers[f"x{i:02d}"] = (x >> i) & 1
        registers[f"y{i:02d}"] = (y >> i) & 1

    # Evaluate instructions
    instruction_indices = list(range(len(instructions)))
    while len(instruction_indices) > 0:
        length = len(instruction_indices)

        for i in range(len(instruction_indices) - 1, -1, -1):
            instr = instructions[instruction_indices[i]]
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
            del instruction_indices[i]

        if len(instruction_indices) == length:
            return -1

    # Construct answer
    answer = 0
    for i in range(N - 1, -1, -1):
        answer = (answer << 1) + registers[f"z{i:02d}"]
    return answer

""" -----------------------------------------------------------------------------------------------|
|                                    Part 2 - Swap instructions                                    |
|----------------------------------------------------------------------------------------------- """

# Create DAG for instruction dependencies
lookup = {instructions[i][3] : i for i in range(len(instructions))}
graph = {}
for instr in instructions:
    graph[instr[3]] = {instr[0], instr[2]}

# Swap 'nnt' and 'gws'
i, j = lookup['nnt'], lookup['gws']
instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
lookup['nnt'], lookup['gws'] = j, i

# Swap 'z13' and 'npf'
i, j = lookup['z13'], lookup['npf']
instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
lookup['z13'], lookup['npf'] = j, i

# Swap 'z19' and 'cph'
i, j = lookup['z19'], lookup['cph']
instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
lookup['z19'], lookup['cph'] = j, i

# Swap 'z33' and 'hgj'
i, j = lookup['z33'], lookup['hgj']
instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
lookup['z33'], lookup['hgj'] = j, i

""" -----------------------------------------------------------------------------------------------|
|                                    Part 2 - Check for issues                                     |
|----------------------------------------------------------------------------------------------- """

for i in range(N - 1):
    bad = False

    x = (1 << (i + 1)) - 1
    y = 0
    z = evaluate(x, y)
    if z != x + y:
        print(f"x = {x:x}, y = {y:x}, z = {z:x}, diff = {(x + y) ^ z:x}")
        bad = True

    y = x
    z = evaluate(x, y)
    if z != x + y:
        print(f"x = {x:x}, y = {y:x}, z = {z:x}, diff = {(x + y) ^ z:x}")
        bad = True

    x = 1 << i
    y = 0
    z = evaluate(x, y)
    if z != x + y:
        print(f"x = {x:x}, y = {y:x}, z = {z:x}, diff = {(x + y) ^ z:x}")
        bad = True

    y = x
    z = evaluate(x, y)
    if z != x + y:
        print(f"x = {x:x}, y = {y:x}, z = {z:x}, diff = {(x + y) ^ z:x}")
        bad = True

    if bad:
        print()

""" -----------------------------------------------------------------------------------------------|
|                             Part 2 - Print instruction dependencies                              |
|----------------------------------------------------------------------------------------------- """

# Print dependencies
roots = [] #["z32", "z33"]
for root in roots:
    print(f"Root = {root}")
    base_dependencies, dependencies = set(), {root}
    while len(dependencies) > 0:
        node = dependencies.pop()
        if node in graph:
            print(instructions[lookup[node]])
            dependencies |= graph[node]
        else:
            base_dependencies.add(node)
    print(f"Base = {base_dependencies}")
    print()

""" -----------------------------------------------------------------------------------------------|
|                                      Part 2 - Print answer                                       |
|----------------------------------------------------------------------------------------------- """

answer = ['nnt', 'gws', 'z13', 'npf', 'z19', 'cph', 'z33', 'hgj']
answer.sort()
print("Answer to part 2 =", answer[0], end = "")
for x in answer[1:]:
    print(f",{x}", end = "")
print()
