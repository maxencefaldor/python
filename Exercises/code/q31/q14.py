class TicTacToeGame:
    def __init__(self, n=3):
        pass  # TODO

    def move(self, r, c):
        pass  # TODO

    def get_winner(self):
        pass  # TODO

    def __str__(self):
        """Helper to print the board (already implemented)"""
        rows = []
        for r in range(self.n):
            rows.append(" | ".join(self.board[r]))
        return "\n".join(rows)
