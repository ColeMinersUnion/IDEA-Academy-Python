try:
    from Pieces.Piece import Piece
except ImportError:
    from Piece import Piece

class Pawn(Piece):
    def __init__(self, color: bool, pos: tuple[int, int] = (0, 0)):
        super().__init__(color, pos)
        self.icon = "\u2659" if color else "\u265F"
        self.has_moved = False
        
    
    def find_moves(self, board: any):
        if self.color: #White pawn
            #Moving forward
            if board.is_empty(self.pos[0], self.pos[1] + 1):
                self.possible_moves.append((self.pos[0], self.pos[1] + 1))
                #Double move from starting position
                if not self.has_moved and board.is_empty(self.pos[0], self.pos[1] + 2):
                    self.possible_moves.append((self.pos[0], self.pos[1] + 2))
            #Capturing diagonally
            if board.is_enemy(self.pos[0] + 1, self.pos[1] + 1, self.color):
                self.possible_moves.append((self.pos[0] + 1, self.pos[1] + 1))
            if board.is_enemy(self.pos[0] - 1, self.pos[1] + 1, self.color):
                self.possible_moves.append((self.pos[0] - 1, self.pos[1] + 1))
        else: #Black Pawn
            if board.is_empty(self.pos[0], self.pos[1] - 1):
                self.possible_moves.append((self.pos[0], self.pos[1] - 1))
                #Double move from starting position
                if not self.has_moved and board.is_empty(self.pos[0], self.pos[1] - 2):
                    self.possible_moves.append((self.pos[0], self.pos[1] - 2))
            #Capturing diagonally
            if board.is_enemy(self.pos[0] + 1, self.pos[1] - 1, self.color):
                self.possible_moves.append((self.pos[0] + 1, self.pos[1] - 1))
            if board.is_enemy(self.pos[0] - 1, self.pos[1] - 1, self.color):
                self.possible_moves.append((self.pos[0] - 1, self.pos[1] - 1))

    def move(self, x: int, y: int):
        if (x, y) not in self.possible_moves:
            raise ValueError(f"Invalid move for Pawn from {self.pos} to {(x, y)}")
        self.pos = (x, y)
        if not self.has_moved:
            self.has_moved = True
        self.possible_moves.clear()

    def get_letter(self):
        return ''  # SAN omits letter for pawn moves

        

    
        
        

    