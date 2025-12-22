from token import NUMBER
from Puzzle_Input import *

codes = ['456A'] #ex_codes

"""
456A

<<^^A>A>AvvA
<<vAA>^AA>AvA^AvA^A<vAA>^A
<<vAA>A>^AAvA<^A>AAvA^A<vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A

v<<A : v<A<AA>>^A
<<vA : v<<AA>A>^A
"""

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

dpad_codes = []
for code in codes:
    dpad = {''}
    y, x = numpad['A']
    for key in code:
        new_y, new_x = numpad[key]
        y_arrows = 'v' * (new_y - y) if new_y > y else '^' * (y - new_y)
        x_arrows = '>' * (new_x - x) if new_x > x else '<' * (x - new_x)

        new_dpad = set()
        if (y < 3 and new_y < 3) or (x > 0 and new_x > 0):
            for command in dpad:
                new_dpad.add(command + y_arrows + x_arrows + 'A')
                new_dpad.add(command + x_arrows + y_arrows + 'A')
        elif x == 0:
            for command in dpad:
                new_dpad.add(command + x_arrows + y_arrows + 'A')
        else:
            for command in dpad:
                new_dpad.add(command + y_arrows + x_arrows + 'A')

        dpad = new_dpad
        y, x = new_y, new_x
    dpad_codes.append(dpad)
complexity = 0
for i in range(len(codes)):
    print(f"P1D0: {codes[i]}: {min({len(x) for x in dpad_codes[i]})} * {int(codes[i][:-1])}")

for number_of_dpad_robots in range(2):
    for i in range(len(codes)):
        new_code = set()
        for code in dpad_codes[i]:
            dpad = {''}
            y, x = dirpad['A']
            for key in code:
                new_y, new_x = dirpad[key]
                y_arrows = 'v' * (new_y - y) if new_y > y else '^' * (y - new_y)
                x_arrows = '>' * (new_x - x) if new_x > x else '<' * (x - new_x)

                new_dpad = set()
                if (y > 0 and new_y > 0) or (x > 0 and new_x > 0):
                    for command in dpad:
                        new_dpad.add(command + y_arrows + x_arrows + 'A')
                        new_dpad.add(command + x_arrows + y_arrows + 'A')
                elif x == 0:
                    for command in dpad:
                        new_dpad.add(command + x_arrows + y_arrows + 'A')
                else:
                    for command in dpad:
                        new_dpad.add(command + y_arrows + x_arrows + 'A')

                dpad = new_dpad
                y, x = new_y, new_x
            new_code |= dpad
        dpad_codes[i] = new_code
    for j in range(len(codes)):
        print(f"P1D{number_of_dpad_robots+1}: {codes[j]}: {min({len(x) for x in dpad_codes[j]})} * {int(codes[j][:-1])}")
print()

""" -----------------------------------------------------------------------------------------------|
|                          Part 2 - Convert numpad codes into dpad codes                           |
|----------------------------------------------------------------------------------------------- """

dpad_codes = []
for code in codes:
    dpad = {'' : 0, '<' : 0, '>' : 0, '^' : 0, 'v' : 0, '<^' : 0, '<v' : 0, '>^' : 0, '>v' : 0}
    y, x = numpad['A']
    for numkey in code:
        new_y, new_x = numpad[numkey]
        dpad['' + ('<' if new_x < x else ('' if new_x == x else '>')) + ('^' if new_y < y else ('' if new_y == y else 'v'))] += 1
        dpad[''] += max(0, abs(new_x - x) - 1) + max(0, abs(new_y - y) - 1)
        y, x = new_y, new_x
    dpad_codes.append(dpad)

""" -----------------------------------------------------------------------------------------------|
|                           Part 2 - Convert dpad codes into dpad codes                            |
|----------------------------------------------------------------------------------------------- """

# print(f"I0: {dpad_codes[2]}")
for number_of_dpad_robots in range(2):
    for i in range(len(codes)):
        code = dpad_codes[i]
        length = code['']
        length += 2 * (code['<'] + code['>'] + code['^'] + code['v'])
        length += 3 * (code['<^'] + code['<v'] + code['>^'] + code['>v'])
        complexity += length * int(codes[i][:-1])
        print(f"P2D{number_of_dpad_robots}: {codes[i]}: {length} * {int(codes[i][:-1])}")

    for i in range(len(dpad_codes)):
        dpad = {'' : 0, '<' : 0, '>' : 0, '^' : 0, 'v' : 0, '<^' : 0, '<v' : 0, '>^' : 0, '>v' : 0}
        for key, val in dpad_codes[i].items():
            # if number_of_dpad_robots == 1 and i == 2:
            #     print(f"key={key :2s}, val={val}, dpad={dpad}")

            if key == '':
                dpad[''] += val

            if key == '^':
                dpad['<'] += val
                dpad['>'] += val
            if key == '>':
                dpad['v'] += val
                dpad['^'] += val
            if key == '<':
                dpad['<v'] += val
                dpad['>^'] += val
                dpad[''] += 2 * val
            if key == 'v':
                dpad['<v'] += val
                dpad['>^'] += val

            if key == '<^' or key == '<v':
                dpad['<v'] += val
                dpad[''] += val
                dpad['>^'] += val
                dpad['>'] += val
            if key == '>^':
                dpad['<'] += val
                dpad['>v'] += val
                dpad['^'] += val
            if key == '>v':
                dpad['v'] += val
                dpad['<'] += val
                dpad['>^'] += val
        dpad_codes[i] = dpad

""" -----------------------------------------------------------------------------------------------|
|                                     Part 2 - Get complexity                                      |
|----------------------------------------------------------------------------------------------- """

complexity = 0
for i in range(len(dpad_codes)):
    code = dpad_codes[i]
    length = code['']
    length += 2 * (code['<'] + code['>'] + code['^'] + code['v'])
    length += 3 * (code['<^'] + code['<v'] + code['>^'] + code['>v'])
    complexity += length * int(codes[i][:-1])
    print(f"P2D2: {codes[i]}: {length} * {int(codes[i][:-1])}")
print("Answer to part 2 =", complexity)
