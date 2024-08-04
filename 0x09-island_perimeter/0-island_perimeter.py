#!/usr/bin/python3

"""Island Perimeter Challenge
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if len(grid) == 0:
        return 0

    countPerimeter = 0
    # loop through each array
    # loop through the array within
    # check for land(i.e values with 1) a the top, bottom, left
    # and right of each point where there is land
    # if next value in any direction is 0, increment countPerimeter,
    # else move to next
    for m, i in enumerate(grid):
        for n, j in enumerate(i):
            if j == 0:
                continue
            # check top and bottom sides
            if grid[m - 1][n] == 0:
                countPerimeter += 1
            if grid[m + 1][n] == 0:
                countPerimeter += 1
            # check left and right sides
            if grid[m][n - 1] == 0:
                countPerimeter += 1
            if grid[m][n + 1] == 0:
                countPerimeter += 1
    return countPerimeter
