def create_board(size=3):
    return [[""] *size for _ in range(size)]

def print_board(board):
    for i, row in enumerate(board):
        print (" | ".join(cell or "-" for cell in row))
        if i<len(board)-1:
            print("--+---+--")
    print()

def is_valid_move(board, row, col):
    size=len(board)
    return 0 <= row < size and 0 <= col < size and board[row][col] == ""

def check_winner(board):
    for i in range(3):
        size=len(board)
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]


    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def is_draw(board):
    return all(cell !="" for row in board for cell in row) and not check_winner(board)


def play_game():
    board= create_board()
    current = "X"

    while True:
        print_board(board)

        try:
            row, col = map(int, input(
                f"Player {current}, enter row and col (1-3): "
                ).split())

        except ValueError:
            print("Please enter two numbers separated by a space.")
            continue

        row -= 1
        col -= 1
        if not is_valid_move(board,row, col):
            print("Invalid move! Try again.")
            continue

        board[row][col] = current
        winner= check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"

play_game()