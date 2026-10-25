"""Experiment 7: Solve the 8-Queens problem using backtracking."""
SIZE = 8


def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < SIZE:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True


def solve(board, row=0):
    if row == SIZE:
        return True
    for col in range(SIZE):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve(board, row + 1):
                return True
            board[row][col] = "."
    return False


def main():
    board = [["." for _ in range(SIZE)] for _ in range(SIZE)]
    if solve(board):
        print("\nSolution for 8-Queens Problem:\n")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
