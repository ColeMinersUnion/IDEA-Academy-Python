try:
    from Pieces.Piece import Piece
except ImportError:
    from Piece import Piece

class King(Piece):
    def __init__(self, color: bool, pos: tuple[int, int] = (0, 0)):
        super().__init__(color, pos)
        self.icon = "\u2654" if color else "\u265A"
        self.has_moved = False

    def find_moves(self, board: any):
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]
        
        for dx, dy in directions:
            new_x = self.pos[0] + dx
            new_y = self.pos[1] + dy
            
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.is_empty(new_x, new_y) and not self.in_check(new_x, new_y, board):
                    self.possible_moves.append((new_x, new_y))
                elif board.is_enemy(new_x, new_y, self.color) and not self.in_check(new_x, new_y, board):
                    self.possible_moves.append((new_x, new_y))
    
    def in_check(self, x: int, y: int, board: any) -> bool:
        for row in board.board:
            for piece in row:
                if piece is not None and piece.color != self.color:
                    if (x, y) in piece.possible_moves:
                        return True
        return False
    
    def move(self, x: int, y: int):
        self.pos = (x, y)
        if not self.has_moved:
            self.has_moved = True
        self.possible_moves.clear()

    def get_letter(self):
        return 'K'
            
                 