from q14 import TicTacToeGame


def test_x_wins_row():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(1, 0)  # o
    game.move(0, 1)  # x
    game.move(1, 1)  # o
    print(game)
    assert game.get_winner() is None
    game.move(0, 2)  # x wins
    print(game)
    assert game.get_winner() == "x"


def test_o_wins_col():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(0, 1)  # o
    game.move(1, 0)  # x
    game.move(1, 1)  # o
    game.move(0, 2)  # x
    print(game)
    assert game.get_winner() is None
    game.move(2, 1)  # o wins
    print(game)
    assert game.get_winner() == "o"


def test_x_wins_diag():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(0, 1)  # o
    game.move(1, 1)  # x
    game.move(0, 2)  # o
    print(game)
    assert game.get_winner() is None
    game.move(2, 2)  # x wins
    print(game)
    assert game.get_winner() == "x"


def test_o_wins_anti_diag():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(0, 2)  # o
    game.move(1, 1)  # x
    game.move(1, 2)  # o
    game.move(2, 2)  # x
    print(game)
    assert game.get_winner() is None
    game.move(2, 0)  # o wins
    print(game)
    assert game.get_winner() == "o"


def test_draw():
    game = TicTacToeGame(3)
    moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 2), (2, 0)]
    # x o x
    # x o o
    # o x x
    game.move(0, 0)  # x
    game.move(0, 1)  # o
    game.move(0, 2)  # x
    game.move(1, 1)  # o
    game.move(1, 0)  # x
    game.move(1, 2)  # o
    game.move(2, 1)  # x
    game.move(2, 2)  # o
    game.move(2, 0)  # x
    print(game)
    assert game.get_winner() == "draw"


def test_4x4_incomplete():
    game = TicTacToeGame(4)
    game.move(0, 0)  # x
    game.move(1, 1)  # o
    game.move(0, 1)  # x
    print(game)
    assert game.get_winner() is None
    assert game.current_player == "o"


def test_invalid_moves():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x

    # Test occupied
    try:
        game.move(0, 0)  # o tries same spot
        assert False, "Did not raise ValueError for occupied cell"
    except ValueError as e:
        print(f"Caught expected error: {e}")
        assert str(e) == "Cell already occupied."

    # Test out of bounds
    try:
        game.move(3, 0)  # o tries out of bounds
        assert False, "Did not raise ValueError for out of bounds"
    except ValueError as e:
        print(f"Caught expected error: {e}")
        assert str(e) == "Move out of bounds."

    # Check player didn't switch
    assert game.current_player == "o"


if __name__ == "__main__":
    test_x_wins_row()
    test_o_wins_col()
    test_x_wins_diag()
    test_o_wins_anti_diag()
    test_draw()
    test_4x4_incomplete()
    test_invalid_moves()
