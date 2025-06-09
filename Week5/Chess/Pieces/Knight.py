try:
    from Pieces.Piece import Piece
except ImportError:
    from Piece import Piece

class Knight(Piece):
    def __init__(self, color: bool, pos: tuple[int, int] = (0, 0)):
        super().__init__(color, pos)
        self.icon = "\u2658" if color else "\u265E"

    def find_moves(self, board: any):
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for dx, dy in knight_moves:
            new_x = self.pos[0] + dx
            new_y = self.pos[1] + dy
            
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.is_empty(new_x, new_y) or board.is_enemy(new_x, new_y, self.color):
                    self.possible_moves.append((new_x, new_y))
    
    def move(self, x: int, y: int):
        if (x, y) not in self.possible_moves:
            raise ValueError(f"Invalid move for Knight from {self.pos} to {(x, y)}")
        self.pos = (x, y)
        self.possible_moves.clear()

    def get_letter(self):
        return 'N'
