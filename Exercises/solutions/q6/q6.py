def flip(grid):
    new_grid = []
    for row in grid:
        new_row = [1 - col for col in row]
        new_grid.append(new_row)
    return new_grid
