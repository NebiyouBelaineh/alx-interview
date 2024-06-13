#!/usr/bin/python3
"""
Module containing minOperations function
"""


def minOperations(n: int) -> int:
    """
    Returns the minimum number of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    # Initialize an array to store minimum operations for each number up to n
    minOps = [float('inf')] * (n + 1)
    minOps[1] = 0  # Base case: 1 H is already there

    # Iterate through each number from 2 to n
    for i in range(2, n + 1):
        # Find minimum operations to achieve i H characters
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                # Calculate operations needed to achieve i from j
                minOps[i] = min(minOps[i], minOps[j] + (i // j))

    # Return the minimum operations needed to achieve n H characters
    return minOps[n]
