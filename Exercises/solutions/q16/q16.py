def is_magic_square(matrix):
    if not are_numbers_in_range(matrix):
        return False

    if has_duplicates(matrix):
        return False

    # get sums for all rows, cols and diagonals
    row_sums = sum_rows(matrix)
    column_sums = sum_columns(matrix)
    diagonal_sums = sum_diagonals(matrix)

    sums = row_sums
    sums.extend(column_sums)
    sums.extend(diagonal_sums)

    return are_sums_equal(sums)


def flatten_matrix(matrix):
    """Return a single flattened list given a 2D matrix."""
    return [col for row in matrix for col in row]


def are_numbers_in_range(matrix):
    """Check whether all numbers in the matrix are in the range 1 - 2^N."""
    n = len(matrix)
    numbers = flatten_matrix(matrix)
    for number in numbers:
        if number < 1 or number > n**2:
            return False
    return True


def has_duplicates(matrix):
    """Check whether there are duplicate numbers in the matrix."""
    numbers = flatten_matrix(matrix)
    return len(set(numbers)) != len(numbers)


def sum_rows(matrix):
    """Return a list containing the sum for each row."""
    total = []
    for row in matrix:
        total.append(sum(row))
    return total


def sum_columns(matrix):
    """Return a list containing the sum for each column."""
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    total = []
    for col_index in range(num_cols):
        total.append(sum(matrix[row_index][col_index] for row_index in range(num_rows)))
    return total


def sum_diagonals(matrix):
    """Return a list containing the sum for the two main diagonals."""
    num_rows = len(matrix)

    # main diagonal
    total_diagonal = sum(matrix[row_index][row_index] for row_index in range(num_rows))

    # counter diagonal
    total_counterdiagonal = sum(
        matrix[num_rows - row_index - 1][row_index] for row_index in range(num_rows)
    )
    return [total_diagonal, total_counterdiagonal]


def are_sums_equal(numbers):
    """Check whether all numbers are equal."""
    return len(set(numbers)) == 1
