from q6 import flip


def test_1x1_grid():
    grid = [[0]]
    result = flip(grid)
    print(result)
    
    expected = [[1]]
    assert result == expected
    
    
def test_2x2_grid():
    grid = [[0, 1],
            [1, 0]]
    result = flip(grid)
    print(result)
    
    expected = [[1, 0], [0, 1]]
    assert result == expected
    
    
def test_2x4_grid():
    grid = [[1, 1, 0, 0],
            [0, 1, 0, 1]]
    result = flip(grid)
    print(result)
    
    expected = [[0, 0, 1, 1], [1, 0, 1, 0]]
    assert result == expected


def test_5x2_grid():
    grid = [[0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1]]
    result = flip(grid)
    print(result)
    
    expected = [[1, 1], [1, 1], [1, 1], [0, 0], [0, 0]]
    assert result == expected


def test_5x5_grid():
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    result = flip(grid)
    print(result)
    
    expected = [[0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 0], 
                [0, 1, 1, 1, 0], 
                [0, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0]]
    assert result == expected
    
    
if __name__ == "__main__":
    test_1x1_grid()
    test_2x2_grid()
    test_2x4_grid()
    test_5x2_grid()
    test_5x5_grid()