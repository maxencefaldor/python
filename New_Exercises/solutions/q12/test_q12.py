from q12 import count_islands


def test_one_island():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print("Testing one island...")
    assert count_islands(grid) == 1


def test_three_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print("Testing three islands...")
    assert count_islands(grid) == 3


def test_no_islands():
    grid = [["0", "0", "0"], ["0", "0", "0"]]
    print("Testing no islands...")
    assert count_islands(grid) == 0


def test_complex_islands():
    grid = [
        ["1", "0", "1", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
    ]
    print("Testing complex islands...")
    assert count_islands(grid) == 4


def test_empty_grid():
    grid = []
    print("Testing empty grid...")
    assert count_islands(grid) == 0


if __name__ == "__main__":
    test_one_island()
    test_three_islands()
    test_no_islands()
    test_complex_islands()
    test_empty_grid()
