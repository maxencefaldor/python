class TicTacToeGame:
    def __init__(self, n=3):
        self.n = n
        # Create an n x n grid filled with spaces
        self.board = [[" " for _ in range(n)] for _ in range(n)]
        self.current_player = "x"
        # Keep track of moves to easily detect a draw
        self.moves_made = 0

    def move(self, r, c):
        # Check for out of bounds
        if not (0 <= r < self.n and 0 <= c < self.n):
            raise ValueError("Move out of bounds.")

        # Check if cell is occupied
        if self.board[r][c] != " ":
            raise ValueError("Cell already occupied.")

        # Place the mark
        self.board[r][c] = self.current_player
        self.moves_made += 1

        # Switch player
        self.current_player = "o" if self.current_player == "x" else "x"

    def get_winner(self):
        n = self.n

        # Check rows and columns
        for i in range(n):
            # Check row i
            if all(self.board[i][j] == "x" for j in range(n)):
                return "x"
            if all(self.board[i][j] == "o" for j in range(n)):
                return "o"

            # Check column i
            if all(self.board[j][i] == "x" for j in range(n)):
                return "x"
            if all(self.board[j][i] == "o" for j in range(n)):
                return "o"

        # Check main diagonal (top-left to bottom-right)
        if all(self.board[i][i] == "x" for i in range(n)):
            return "x"
        if all(self.board[i][i] == "o" for i in range(n)):
            return "o"

        # Check anti-diagonal (top-right to bottom-left)
        if all(self.board[i][n - 1 - i] == "x" for i in range(n)):
            return "x"
        if all(self.board[i][n - 1 - i] == "o" for i in range(n)):
            return "o"

        # Check for draw (all cells full, no winner)
        if self.moves_made == n * n:
            return "draw"

        # No winner yet, and game is not over
        return None

    def __str__(self):
        """Helper to print the board (already implemented)"""
        # Create a horizontal separator
        separator = "\n" + ("---" * self.n) + ("-" * (self.n - 1)) + "\n"

        rows = []
        for r in range(self.n):
            # Join cells with " | "
            rows.append(" | ".join(self.board[r]))

        # Join rows with the separator
        return separator.join(rows)
