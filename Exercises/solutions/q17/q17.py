def can_exit_maze(maze):
    # Get set of coords for cells that are unobstructed
    unobstructed_cells = set(
        [
            (r, c)
            for (r, row) in enumerate(maze)
            for (c, cell) in enumerate(row)
            if cell == 0
        ]
    )

    # Set target cell to bottom left
    target_cell = (len(maze) - 1, len(maze[0]) - 1)

    # Don't waste time if exit is obstructed
    if target_cell not in unobstructed_cells:
        return False

    # Can assume that (0,0) is always in the set
    current_cell = (0, 0)

    # Mark current cell as seen (by removing from the set)
    unobstructed_cells.remove(current_cell)

    # Get unobstructed neighbours of the current cell
    neighbours = get_neighbours(current_cell, unobstructed_cells)

    while len(neighbours) > 0:
        # Pick next cell in list of neighbours
        current_cell = neighbours.pop()

        # Remove cell from valid candidate pool (since already seen)
        unobstructed_cells.remove(current_cell)

        if current_cell == target_cell:
            return True
        else:
            # Add new neighbours to unexplored neighbour set
            neighbours.update(get_neighbours(current_cell, unobstructed_cells))

    return False


def get_neighbours(cell, valid_cells):
    """Get 4-neighbours of a given cell, given a set of valid (unexplored) cells."""
    row, col = cell
    neighbours = set()
    if (row - 1, col) in valid_cells:
        neighbours.add((row - 1, col))
    if (row + 1, col) in valid_cells:
        neighbours.add((row + 1, col))
    if (row, col - 1) in valid_cells:
        neighbours.add((row, col - 1))
    if (row, col + 1) in valid_cells:
        neighbours.add((row, col + 1))
    return neighbours
