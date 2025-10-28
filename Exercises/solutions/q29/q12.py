def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    # We will modify the grid in-place by changing "1" to "#"
    # to mark visited land cells.

    def dfs(r, c):
        """Depth-First Search to find all connected land."""

        # Base case: Check for out-of-bounds or if it's water/visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        # Mark the current cell as visited
        grid[r][c] = "#"

        # Recursively visit all 4 neighbors
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Main loop to iterate through every cell
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell ("1"), it's a new island
            if grid[r][c] == "1":
                island_count += 1
                # Start a DFS to "sink" all parts of this island
                dfs(r, c)

    return island_count
