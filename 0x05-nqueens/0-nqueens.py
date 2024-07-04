#!/usr/bin/env python3

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    This function checks the column and the two diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print all solutions
    """
    def solve(row):
        if row == N:
            # Found a solution, add it to the list
            solutions.append(board[:])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1)
                    board[row] = -1

    board = [-1] * N
    solutions = []
    solve(0)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions in the required format
    """
    for solution in solutions:
        print("[", end="")
        print(", ".join(
            f"[{i}, {col}]" for i, col in enumerate(solution)), end="")
        print("]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
