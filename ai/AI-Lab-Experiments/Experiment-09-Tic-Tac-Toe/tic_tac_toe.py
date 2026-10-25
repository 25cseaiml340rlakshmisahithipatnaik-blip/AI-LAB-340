"""Experiment 9: Two-player Tic-Tac-Toe."""

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("---------")


def check_winner(board):
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)]
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    return any(line[0] and line[0] == line[1] == line[2] for line in lines)


def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0
    while moves < 9:
        print("\nCurrent Board:")
        print_board(board)
        print(f"Player {player}'s Turn")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Please enter numbers from 0 to 2.")
            continue
        if row not in range(3) or col not in range(3):
            print("Row and column must be between 0 and 2.")
            continue
        if board[row][col]:
            print("Cell already occupied. Try again.")
            continue
        board[row][col] = player
        moves += 1
        if check_winner(board):
            print("\nFinal Board:")
            print_board(board)
            print(f"Player {player} Wins!")
            return
        player = "O" if player == "X" else "X"
    print("\nFinal Board:")
    print_board(board)
    print("Game Draw!")

if __name__ == "__main__":
    main()
