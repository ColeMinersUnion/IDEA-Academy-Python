import re
from typing import Generator


def replay_game(path: str) -> Generator[str, None, None]:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Join lines, skip metadata
    game_text = " ".join(line.strip() for line in lines if not line.startswith("["))
    
    # Remove comments { ... }
    game_text = re.sub(r"\{[^}]*\}", "", game_text)
    
    # Remove variations ( ... )
    game_text = re.sub(r"\([^)]*\)", "", game_text)
    
    # Remove result at end (e.g., 1-0, 0-1, 1/2-1/2)
    game_text = re.sub(r"\d-\d|\d/\d-\d/\d", "", game_text)
    
    # Remove annotations (e.g., !, ?, !?, ??)
    game_text = re.sub(r"[\!\?]+", "", game_text)

    # Remove move numbers (e.g., 1., 2.)
    game_text = re.sub(r"\d+\.(\.\.)?", "", game_text)

    # Collapse extra whitespace
    tokens = game_text.strip().split()

    for move in tokens:
        yield move

            