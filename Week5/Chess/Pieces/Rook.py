try:
    from Pieces.Piece import Piece
except ImportError:
    from Piece import Piece

class Rook(Piece):
    def __init__(self, color: bool, pos: tuple[int, int] = (0, 0)):
        super().__init__(color, pos)
        self.icon = "\u2656" if color else "\u265C"
        self.has_moved = False

    def find_moves(self, board: any):
        #North
        x, y = self.pos
        while(True):
            y += 1
            if not (0 <= y < 8):
                break
            if board.is_empty(x, y):
                self.possible_moves.append((x, y))
            elif board.is_enemy(x, y, self.color):
                self.possible_moves.append((x, y))
                break
            else:
                break
        #South
        x, y = self.pos
        while(True):
            y -= 1
            if not (0 <= y < 8):
                break
            if board.is_empty(x, y):
                self.possible_moves.append((x, y))
            elif board.is_enemy(x, y, self.color):
                self.possible_moves.append((x, y))
                break
            else:
                break
        #East (Right)
        x, y = self.pos
        while(True):
            x += 1
            if not (0 <= x < 8):
                break
            if board.is_empty(x, y):
                self.possible_moves.append((x, y))
            elif board.is_enemy(x, y, self.color):
                self.possible_moves.append((x, y))
                break
            else:
                break
        #West (Left)
        x, y = self.pos
        while(True):
            x -= 1
            if not (0 <= x < 8):
                break
            if board.is_empty(x, y):
                self.possible_moves.append((x, y))
            elif board.is_enemy(x, y, self.color):
                self.possible_moves.append((x, y))
                break
            else:
                break
        
    def move(self, x: int, y: int):
        self.pos = (x, y)
        if not self.has_moved:
            self.has_moved = True
        self.possible_moves.clear()

    def get_letter(self):
        return 'R'
