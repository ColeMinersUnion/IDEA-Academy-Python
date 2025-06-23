from Board import Board
from time import sleep
from Helpers.GameReplay import replay_game
from os import path
from Helpers.ParseSAN import parse_san_move


   

board = Board()
turn = True
print(board)


game_path = path.join(path.dirname(__file__), "Games", "PromotionTest.pgn")

for move in replay_game(game_path):
    if move.strip() == "O-O":
        board.castle(True, turn)
    elif move.strip() == "O-O-O":
        board.castle(False, turn)
    else:
        from_pos, to_pos, promotion = parse_san_move(move, board, turn)
        board.move_piece(from_pos, to_pos)
        if promotion:
            board.promote(to_pos, promotion)
    print(board)
    print(f"Move {move} executed successfully.")
    turn = not turn  # Switch turns
    sleep(0.5)
    board.regenerate_possible_moves()
print(board.board[7][7].possible_moves)




# while True:
    

#     move = input("Enter your move in SAN format: ")
#     if move.strip() == "O-O":
#         board.castle(True, turn)
#     elif move.strip() == "O-O-O":
#         board.castle(False, turn)
#     else:
#         from_pos, to_pos, promotion = parse_san_move(move, board, turn)
#         board.move_piece(from_pos, to_pos)
#         if promotion:
#             board.promote(to_pos, promotion)
#     print(board)
#     print(f"Move {move} executed successfully.")
#     turn = not turn  # Switch turns
#     board.regenerate_possible_moves()


