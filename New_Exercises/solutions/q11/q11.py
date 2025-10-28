def rotate_matrix(matrix):
    """
    Rotates an NxN matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    # 1. Transpose the matrix
    # (Swap rows with columns)
    # We only need to iterate over the upper triangle (j > i)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap element (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row
    for i in range(n):
        matrix[i].reverse()

    # No return value is needed as the matrix is modified in-place.
