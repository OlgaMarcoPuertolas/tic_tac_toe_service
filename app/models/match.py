class Match:
    def __init__(self, match_id):
        self.match_id = match_id
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.over = False

    def to_dict(self):
        return {
            "matchId": self.match_id,
            "board": self.board,
            "currentPlayer": self.current_player,
            "winner": self.winner,
            "over": self.over
        }
