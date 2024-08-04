#!/usr/bin/python3

"""Island Perimeter Challenge
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid or len(grid) == 0:
        return 0
    if len(grid) > 100 or len(grid[0]) > 100:
        return 0

    countPerimeter = 0
    # loop through each array
    # loop through the array within
    # check for land(i.e values with 1) a the top, bottom, left
    # and right of each point where there is land
    # if next value in any direction is 0, increment countPerimeter,
    # else move to next
    rows = len(grid)
    cols = len(grid[0])
    for m in range(rows):
        for n in range(cols):
            if grid[m][n] == 1:
                # check top and bottom sides
                if m == 0 or grid[m - 1][n] == 0:
                    countPerimeter += 1
                if m == rows - 1 or grid[m + 1][n] == 0:
                    countPerimeter += 1
                # check left and right sides
                if n == 0 or grid[m][n - 1] == 0:
                    countPerimeter += 1
                if n == cols - 1 or grid[m][n + 1] == 0:
                    countPerimeter += 1
    return countPerimeter
