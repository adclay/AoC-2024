from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 2                                              |
|----------------------------------------------------------------------------------------------- """

cost = 0
for y in range(plot.shape[0]):
    for x in range(plot.shape[1]):
        if plot[y, x] == '.':
            continue
        
        # Replace region with '-' and create set of fenceposts
        crop, search, fence = plot[y, x], {(y, x)}, set()
        while len(search) > 0:
            Y, X = search.pop()
            if plot[Y, X] == crop:
                plot[Y, X] = '-'
                if Y == 0 or (plot[Y - 1, X] != '-' and plot[Y - 1, X] != crop):
                    fence.add((2 * Y - 1, 2 * X, 'N'))
                elif plot[Y - 1, X] == crop:
                    search.add((Y - 1, X))
                    
                if Y == plot.shape[0] - 1 or (plot[Y + 1, X] != '-' and plot[Y + 1, X] != crop):
                    fence.add((2 * Y + 1, 2 * X, 'S'))
                elif plot[Y + 1, X] == crop:
                    search.add((Y + 1, X))
                    
                if X == 0 or (plot[Y, X - 1] != '-' and plot[Y, X - 1] != crop):
                    fence.add((2 * Y, 2 * X - 1, 'W'))
                elif plot[Y, X - 1] == crop:
                    search.add((Y, X - 1))
                    
                if X == plot.shape[1] - 1 or (plot[Y, X + 1] != '-' and plot[Y, X + 1] != crop):
                    fence.add((2 * Y, 2 * X + 1, 'E'))
                elif plot[Y, X + 1] == crop:
                    search.add((Y, X + 1))
        
        # Calculate sides of region
        sides = 0
        while len(fence) > 0:
            sides += 1
            Y, X, direction = fence.pop()
            if Y % 2:
                left, right = X - 2, X + 2
                while (Y, left, direction) in fence:
                    fence.remove((Y, left, direction))
                    left -= 2
                while (Y, right, direction) in fence:
                    fence.remove((Y, right, direction))
                    right += 2
            else:
                left, right = Y - 2, Y + 2
                while (left, X, direction) in fence:
                    fence.remove((left, X, direction))
                    left -= 2
                while (right, X, direction) in fence:
                    fence.remove((right, X, direction))
                    right += 2
             
        # Clean up
        cost += sides * len(plot[plot == '-'])
        plot[plot == '-'] = '.'
print("Answer to part 2 =", cost)
