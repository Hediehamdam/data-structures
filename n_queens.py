"""
File Name: n_queens.py
Description: Solves the N-Queens problem (8x8 chessboard) using Backtracking.
Data Structure/Algorithm: 8x8 Matrix, Backtracking
Operations: place_queen, is_safe, print_board
Use Case: Classic AI problem, practicing constraint satisfaction
"""

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper-left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    # Check upper-right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print_board(board)
        return True  # prints first solution only; remove to print all
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens(board, row+1, N):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    N = 8
    board = [[0]*N for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No solution exists.")
