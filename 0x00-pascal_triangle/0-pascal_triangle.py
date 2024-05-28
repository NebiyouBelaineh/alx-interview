#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Returns the pascal triangle representation of the nth row"""
    if n <= 0:
        # Returns an empty list if n is less than or equal to 0
        return []
    # Pascal's triangle starts with a single value of 1
    result = [[1]]
    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        # each number is added to the next to find next number in the row
        row = [temp[j] + temp[j + 1] for j in range(len(result[-1]) + 1)]
        result.append(row)
    return result
