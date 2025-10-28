from q16 import is_magic_square


def test_1x1_magic():
    matrix = [[1]]
    result = is_magic_square(matrix)
    print(result)
    assert result == True
    
    
def test_1x1_not_magic():
    matrix = [[5]]
    result = is_magic_square(matrix)
    print(result)
    assert result == False
    
    
def test_3x3_magic():
    matrix = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == True


def test_3x3_out_of_bounds_number():
    matrix = [
        [8, 11, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == False
    
    
def test_3x3_repeated_number():
    matrix = [
        [8, 1, 7],
        [3, 5, 7],
        [4, 9, 2]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == False
    
    
def test_3x3_bad_row_sum():
    matrix = [
        [8, 2, 6],
        [3, 5, 7],
        [4, 9, 1]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == False


def test_3x3_bad_diagonal_sum():
    matrix = [
        [1, 5, 9],
        [6, 7, 2],
        [8, 3, 4]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == False
    
    
def test_6x6_magic():
    matrix = [
        [35, 1, 6, 26, 19, 24],
        [3, 32, 7, 21, 23, 25],
        [31, 9, 2, 22, 27, 20],
        [8, 28, 33, 17, 10, 15],
        [30, 5, 34, 12, 14, 16],
        [4, 36, 29, 13, 18, 11]
    ]
    result = is_magic_square(matrix)
    print(result)
    assert result == True

    
if __name__ == "__main__":
    test_3x3_magic()
    test_3x3_out_of_bounds_number()
    test_3x3_repeated_number()
    test_3x3_bad_row_sum()
    test_3x3_bad_diagonal_sum()
    test_6x6_magic()
    test_1x1_magic()
    test_1x1_not_magic()