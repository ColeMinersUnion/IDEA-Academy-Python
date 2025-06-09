class Piece:
    def __init__(self, color: bool, pos: tuple[int, int] = (0, 0)):
        self.color = color
        self.icon = "\u2659" if color else "\u265F"
        self.pos = pos
        self.possible_moves = []

    def __str__(self):
        return f"{self.icon}"
    
    def get_letter(self):
        raise NotImplementedError("Must implement get_letter in subclass")

    
    

    
