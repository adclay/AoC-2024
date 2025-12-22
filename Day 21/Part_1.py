from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                          Part 1 - Convert numpad codes into dpad codes                           |
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

""" -----------------------------------------------------------------------------------------------|
|                           Part 1 - Convert dpad codes into dpad codes                            |
|----------------------------------------------------------------------------------------------- """

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

""" -----------------------------------------------------------------------------------------------|
|                                     Part 1 - Get complexity                                      |
|----------------------------------------------------------------------------------------------- """

complexity = 0
for i in range(len(codes)):
    complexity += min({len(x) for x in dpad_codes[i]}) * int(codes[i][:-1])
print("Answer to part 1 =", complexity)
