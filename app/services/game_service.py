import uuid
from app.models.match import Match

matches = {}

def create_match():
    match_id = str(uuid.uuid4())
    match = Match(match_id)
    matches[match_id] = match
    return match_id

def get_match(match_id):
    return matches.get(match_id)

def make_move(match_id, player, x, y):
    match = matches.get(match_id)
    if not match or match.over:
        return None

    if player != match.current_player:
        return match.to_dict()

    if match.board[x-1][y-1] != "":
        return match.to_dict()

    match.board[x-1][y-1] = player
    if check_winner(match.board, player):
        match.winner = player
        match.over = True
    elif all(cell for row in match.board for cell in row):
        match.over = True
    else:
        match.current_player = "O" if player == "X" else "X"

    return match.to_dict()

def check_winner(board, player):
    win_lines = (
        [row for row in board] +
        [[board[r][c] for r in range(3)] for c in range(3)] +
        [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    )
    return any(all(cell == player for cell in line) for line in win_lines)
