"""
Functions
Terminal Two Player Tic-Tac-Toe Game

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9


"""
board = [None] * 9

def helper():
    key_board = [" " + str(i) + " " for i in range(1,10)]
    print("Welcome to Tic-Tac-Toe!")
    for i in range(3):
        print("|".join(key_board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")
    print("\n")

def print_board(board: list):
    
    # Convert board to strings
    def convert_to_str(board):
        return [" X " if x and x is not None else " O " if not x and x is not None else '   ' for x in board]
    board = convert_to_str(board)
    print("\n")
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_for_winner(board: list):
    # Check rows, columns, and diagonals for a winner
    # Explicitly defined winning combos
    # Technically faster, but feels like a hack
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    for a, b, c in winning_combinations:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def play():
    current_player = True  # True for player X, False for player O
    moves = 0
    
    while moves < 9:
        print_board(board)
        move = input(f"Player {'X' if current_player else 'O'}, enter your move (1-9): ")
        
        try:
            move = int(move) - 1
            if move < 0 or move >= 9 or board[move] is not None:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        board[move] = current_player
        moves += 1
        
        winner = check_for_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Player {'X' if winner else 'O'} wins!")
            return
        
        current_player = not current_player
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    helper()
    play()
