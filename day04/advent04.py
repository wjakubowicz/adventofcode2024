def read_grid(filename):
    with open(filename) as f:
        return f.read().splitlines()

def count_occurrences(grid, target="XMAS"):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),   # Right:    row stays same, column increases
        (0, -1),  # Left:     row stays same, column decreases
        (1, 0),   # Down:     row increases, column stays same
        (-1, 0),  # Up:       row decreases, column stays same
        (1, 1),   # Diagonal: row increases, column increases
        (1, -1),  # Diagonal: row increases, column decreases
        (-1, 1),  # Diagonal: row decreases, column increases
        (-1, -1)  # Diagonal: row decreases, column decreases
    ]
    count = 0
    target_len = len(target)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != target[0]:  # Early skip if first letter doesn't match
                continue
            for dr, dc in directions: # # Calculate the end position of the target string in the current direction
                end_r, end_c = r + dr * (target_len - 1), c + dc * (target_len - 1)
                if 0 <= end_r < rows and 0 <= end_c < cols: # Check if the end position is within the grid bounds
                    if all(grid[r + dr * i][c + dc * i] == target[i] for i in range(target_len)):
                        count += 1
                    
    return count

def count_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def check_diagonal_mas(r, c, dr, dc):
        if grid[r][c] != 'A': # Must have 'A' at center
            return False
            
        # Check that both ends are within grid bounds
        if (0 <= r-dr < rows and 0 <= c-dc < cols and 0 <= r+dr < rows and 0 <= c+dc < cols):
            upper = grid[r-dr][c-dc]
            lower = grid[r+dr][c+dc]
            # Valid if M-A-S or S-A-M pattern
            return (upper == 'M' and lower == 'S') or (upper == 'S' and lower == 'M')
        return False

    for r in range(rows): # Check each position for valid center 'A'
        for c in range(cols):
            if grid[r][c] == 'A':
                # Must have valid patterns in both diagonals
                if check_diagonal_mas(r, c, 1, 1) and check_diagonal_mas(r, c, 1, -1):
                    count += 1
    return count

if __name__ == "__main__":
    grid = read_grid("advent04.txt")
    print(count_occurrences(grid))
    print(count_xmas_occurrences(grid))