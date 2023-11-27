#!/usr/bin/python3
from sys import argv

def print_solution(solutions):
    """
    Prints each solution of the N-Queens problem.

    Args:
    - solutions: List of solutions, where each solution is a list of [row, col] pairs.
    """
    for solution in solutions:
        print(solution)

def is_safe(tested, row, col):
    """
    Checks if placing a queen at a given position is safe.

    Args:
    - tested: List containing the column index for each row where a queen is placed.
    - row: Row index.
    - col: Column index.

    Returns:
    - True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if tested[i] == col or abs(tested[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    """
    Solves the N-Queens problem for a given board size.

    Args:
    - N: Integer representing the board size.

    Returns:
    - List of solutions where each solution is represented as a list of [row, col] pairs.
    """
    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = []

    def solve(tested, row):
        """Recursive function to solve the N-Queens problem."""
        if row == N:
            solutions.append([[q, tested[q]] for q in range(N)])
            return
        for col in range(N):
            if is_safe(tested, row, col):
                tested[row] = col
                solve(tested, row + 1)

    tested = [-1] * N
    solve(tested, 0)
    return solutions

if __name__ == "__main__":
    # Check for correct usage
    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    # Solve the N-Queens problem and print solutions
    solutions = solve_nqueens(N)
    print_solution(solutions)
