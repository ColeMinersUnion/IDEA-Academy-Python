from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen

from Helpers.Timing import timing_decorator



class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.reset_board()

    def __str__(self):
        output = ""
        for row in reversed(self.board):
            for piece in row:
                if piece is None:
                    output += " . "
                else:
                    output += f" {str(piece)} "
            output += "\n"
            
        return output

    def reset_board(self):
        #Add Pawns
        for i in range(8):
            self.board[1][i] = Pawn(True, (i, 1)) #White Pawns
            self.board[6][i] = Pawn(False, (i, 6)) #Black Pawns
        #Kings
        self.board[0][4] = King(True, (4, 0))  # White King
        self.board[7][4] = King(False, (4, 7)) # Black King
        
        #Queens
        self.board[0][3] = Queen(True, (3, 0))
        self.board[7][3] = Queen(False, (3, 7))

        #Rooks
        self.board[0][0] = Rook(True, (0, 0))
        self.board[0][7] = Rook(True, (7, 0))
        self.board[7][0] = Rook(False, (0, 7))
        self.board[7][7] = Rook(False, (7, 7))
        
        #Knights
        self.board[0][1] = Knight(True, (1, 0))
        self.board[0][6] = Knight(True, (6, 0))
        self.board[7][1] = Knight(False, (1, 7))
        self.board[7][6] = Knight(False, (6, 7))

        #Bishops
        self.board[0][2] = Bishop(True, (2, 0))
        self.board[0][5] = Bishop(True, (5, 0))
        self.board[7][2] = Bishop(False, (2, 7))
        self.board[7][5] = Bishop(False, (5, 7))
        



    def is_empty(self, x: int, y: int) -> bool:
        try:
            return self.board[y][x] is None
        except IndexError:
            return False
        
    def is_enemy(self, x: int, y: int, color: bool) -> bool:
        try:
            piece = self.board[y][x]
            return piece is not None and piece.color != color
        except IndexError:
            return False
        
    @timing_decorator
    def move_piece(self, old_pos: tuple[int, int], new_pos: tuple[int, int]):
        if self.board[old_pos[1]][old_pos[0]] is None:
            raise ValueError(f"No piece at position {old_pos}")
        piece = self.board[old_pos[1]][old_pos[0]]
        if new_pos not in piece.possible_moves:
            raise ValueError(f"Invalid move for {piece} from {old_pos} to {new_pos}")
        self.board[new_pos[1]][new_pos[0]] = piece
        self.board[old_pos[1]][old_pos[0]] = None
        piece.move(new_pos[0], new_pos[1])
        self.regenerate_possible_moves()

    def force_move(self, old_pos: tuple[int, int], new_pos: tuple[int, int]):
        if self.board[old_pos[1]][old_pos[0]] is None:
            raise ValueError(f"No piece at position {old_pos}")
        
        piece = self.board[old_pos[1]][old_pos[0]]
        self.board[new_pos[1]][new_pos[0]] = piece
        self.board[old_pos[1]][old_pos[0]] = None
        piece.move(new_pos[0], new_pos[1])

    def can_castle(self, short_castle: bool, color: bool) -> bool:
        # NOTE: this does not watch for check conditions that prevent castling.
        if color:
            if short_castle: # White short castle
                return (self.is_empty(5, 0) and self.is_empty(6, 0) and
                        self.board[0][4] is not None and not self.board[0][4].has_moved and
                        self.board[0][7] is not None and not self.board[0][7].has_moved)
            else: # White long castle
                return (self.is_empty(1, 0) and self.is_empty(2, 0) and self.is_empty(3, 0) and
                        self.board[0][4] is not None and not self.board[0][4].has_moved and
                        self.board[0][0] is not None and not self.board[0][0].has_moved)
        else:
            if short_castle:
                return (self.is_empty(5, 7) and self.is_empty(6, 7) and
                        self.board[7][4] is not None and not self.board[7][4].has_moved and
                        self.board[7][7] is not None and not self.board[7][7].has_moved)
            else:
                return (self.is_empty(1, 7) and self.is_empty(2, 7) and self.is_empty(3, 7) and
                        self.board[7][4] is not None and not self.board[7][4].has_moved and
                        self.board[7][0] is not None and not self.board[7][0].has_moved)
            
    
    def castle(self, short_castle: bool, color: bool):
        if not self.can_castle(short_castle, color):
            raise ValueError("Castling is not allowed in this position")
        if color:
            if short_castle:
                self.force_move((4, 0), (6, 0))
                self.force_move((7, 0), (5, 0))
            else:
                self.force_move((4, 0), (2, 0))
                self.force_move((0, 0), (3, 0))
        else:
            if short_castle:
                self.force_move((4, 7), (6, 7))
                self.force_move((7, 7), (5, 7))
            else:
                self.force_move((4, 7), (2, 7))
                self.force_move((0, 7), (3, 7))
    
           
    
    def regenerate_possible_moves(self):
        for row in self.board:
            for piece in row:
                if piece is not None:
                    piece.find_moves(self)


if __name__ == "__main__":
    board = Board()
    print(board)    
    # Example of moving a pawn
    
