from q11 import rotate_matrix
import copy


def test_3x3():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # We use copy.deepcopy to check the *original* object was modified
    matrix_to_modify = copy.deepcopy(matrix)

    rotate_matrix(matrix_to_modify)

    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    print("Original:", matrix)
    print("Rotated:", matrix_to_modify)

    assert matrix_to_modify == expected
    assert matrix_to_modify is not matrix  # Sanity check: ensure it's a new object
    assert matrix_to_modify != matrix  # Ensure modification happened


def test_4x4():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    matrix_to_modify = copy.deepcopy(matrix)

    rotate_matrix(matrix_to_modify)

    expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    print("Original:", matrix)
    print("Rotated:", matrix_to_modify)

    assert matrix_to_modify == expected


def test_1x1():
    matrix = [[42]]
    matrix_to_modify = copy.deepcopy(matrix)
    rotate_matrix(matrix_to_modify)
    expected = [[42]]

    print("Rotated:", matrix_to_modify)
    assert matrix_to_modify == expected


def test_2x2():
    matrix = [[1, 2], [3, 4]]
    matrix_to_modify = copy.deepcopy(matrix)
    rotate_matrix(matrix_to_modify)
    expected = [[3, 1], [4, 2]]

    print("Rotated:", matrix_to_modify)
    assert matrix_to_modify == expected


if __name__ == "__main__":
    test_3x3()
    test_4x4()
    test_1x1()
    test_2x2()
