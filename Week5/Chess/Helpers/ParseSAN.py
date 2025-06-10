import re
try:
    from Timing import timing_decorator
except ImportError:
    from Helpers.Timing import timing_decorator

#Written by: GPT-4o
@timing_decorator
def parse_san_move(move_str: str, board, white_to_move: bool) -> tuple[tuple[int, int], tuple[int, int]]:
    move_str = move_str.strip()
    color = white_to_move

    board.regenerate_possible_moves()

    # --- Handle castling ---
    if move_str in ("O-O", "0-0"):
        return ((4, 0) if color else (4, 7), (6, 0) if color else (6, 7))
    if move_str in ("O-O-O", "0-0-0"):
        return ((4, 0) if color else (4, 7), (2, 0) if color else (2, 7))

    # --- Parse the SAN ---
    pattern = r"^(?P<piece>[KQRBN])?"                  # Optional piece letter
    pattern += r"(?P<disambiguate>[a-h1-8]{0,2})"      # Optional disambiguation
    pattern += r"(x)?"                                 # Optional capture
    pattern += r"(?P<target>[a-h][1-8])"               # Target square
    pattern += r"(=?(?P<promotion>[QRBN]))?"           # Optional promotion
    pattern += r"[+#]?$"                               # Optional check/mate

    match = re.match(pattern, move_str)
    if not match:
        raise ValueError(f"Invalid move string: {move_str}")
    
    def algebraic_to_coords(square: str) -> tuple[int, int]:
        file = ord(square[0]) - ord('a')
        rank = int(square[1]) - 1
        return (file, rank)

    piece_letter = match.group("piece") or ""  # Blank = pawn
    disambiguate = match.group("disambiguate")
    target_square = match.group("target")
    promotion_piece = match.group("promotion")
    to_x, to_y = algebraic_to_coords(target_square)

    # --- Identify matching pieces on the board ---
    candidates = []
    for row in board.board:
        for piece in row:
            if piece is None or piece.color != color:
                continue
            if piece.get_letter() != piece_letter:
                continue
            if (to_x, to_y) not in piece.possible_moves:
                continue
            candidates.append(piece)

    # --- Apply disambiguation ---
    if disambiguate:
        filtered = []
        for piece in candidates:
            file_match = disambiguate in "abcdefgh" and piece.pos[0] == ord(disambiguate[0]) - ord('a')
            rank_match = disambiguate in "12345678" and piece.pos[1] == int(disambiguate[0]) - 1
            file_rank_match = len(disambiguate) == 2 and (
                piece.pos[0] == ord(disambiguate[0]) - ord('a') and
                piece.pos[1] == int(disambiguate[1]) - 1
            )
            if file_match or rank_match or file_rank_match:
                filtered.append(piece)
        candidates = filtered

    if len(candidates) == 0:
        raise ValueError(f"No legal piece found for move: {move_str}")
    if len(candidates) > 1:
        raise ValueError(f"Ambiguous move: {move_str}, candidates: {[p.pos for p in candidates]}")


    from_x, from_y = candidates[0].pos
    return (from_x, from_y), (to_x, to_y), promotion_piece if promotion_piece else None
 