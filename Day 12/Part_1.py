from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

cost = 0
for y in range(plot.shape[0]):
    for x in range(plot.shape[1]):
        if plot[y, x] == '.':
            continue
        
        # Replace region with '-'
        crop, search = plot[y, x], {(y, x)}
        while len(search) > 0:
            Y, X = search.pop()
            if Y < 0 or X < 0 or Y > plot.shape[0] - 1 or X > plot.shape[1] - 1:
                continue
            if plot[Y, X] == crop:
                plot[Y, X] = '-'
                search.add((Y - 1, X))
                search.add((Y + 1, X))
                search.add((Y, X - 1))
                search.add((Y, X + 1))
        
        # Calculate perimeter of region
        perimeter, region = 0, np.where(plot == '-')
        region = [(region[0][i], region[1][i]) for i in range(len(region[0]))]
        for Y, X in region:
            if Y == 0 or plot[Y - 1, X] != '-':
                perimeter += 1
            if Y == plot.shape[0] - 1 or plot[Y + 1, X] != '-':
                perimeter += 1
            if X == 0 or plot[Y, X - 1] != '-':
                perimeter += 1
            if X == plot.shape[1] - 1 or plot[Y, X + 1] != '-':
                perimeter += 1
             
        # Clean up
        plot[plot == '-'] = '.'
        cost += perimeter * len(region)
print("Answer to part 1 =", cost)
