EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def get_empty_cells(board):
    # Return a list of empty cells
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return -1
    if is_winner(board, PLAYER_O):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = None
    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_O
        move_val = minimax(board, 0, False)
        board[i][j] = EMPTY
        if move_val > best_val:
            move = (i, j)
            best_val = move_val
    return move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print_board(board)

    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_X
        else:
            print("Cell already occupied. Try again.")
            continue

        print_board(board)

        if is_winner(board, PLAYER_X):
            print("Player X wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # Bot's move
        print("Bot's move:")
        row, col = best_move(board)
        board[row][col] = PLAYER_O

        print_board(board)

        if is_winner(board, PLAYER_O):
            print("Bot O wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
