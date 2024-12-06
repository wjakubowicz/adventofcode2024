def solve_guard_path(input_data, part2=False): # Solve the problem for Part 1 or Part 2
    grid = [list(line) for line in input_data.splitlines()]
    height, width = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # UP, RIGHT, DOWN, LEFT

    # Find the starting position of the guard (^) in the grid
    start = next(((x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == '^'), None)
    if not start:
        return "No starting position found"
    
    x, y = start

    def simulate_guard(y, x, check_loop=False): # Simulate the guard's path and return the number of unique positions visited or detect loops
        visited = set()
        dir_idx = 0  # Start facing UP
        
        while True:
            dy, dx = directions[dir_idx]
            new_y, new_x = y + dy, x + dx
            
            if not (0 <= new_y < height and 0 <= new_x < width):
                break  # Guard leaves the grid
            
            while grid[new_y][new_x] == "#":
                dir_idx = (dir_idx + 1) % 4  # Turn clockwise
                dy, dx = directions[dir_idx]
                new_y, new_x = y + dy, x + dx
                if not (0 <= new_y < height and 0 <= new_x < width):
                    return len(visited) + 1 if not check_loop else False
            
            state = (new_y, new_x, dir_idx)
            if check_loop:
                if state in visited:
                    return True  # Infinite loop detected
                visited.add(state)
            else:
                visited.add((new_y, new_x))
            
            y, x = new_y, new_x

        return len(visited) + 1 if not check_loop else False

    if not part2:
        return simulate_guard(y, x)
    
    # Part 2: Count blocking positions that create a loop
    count = 0
    for y2 in range(height):
        for x2 in range(width):
            if grid[y2][x2] == ".":
                grid[y2][x2] = "#"  # Temporarily block this position
                if simulate_guard(y, x, check_loop=True):
                    count += 1
                grid[y2][x2] = "."  # Restore original position
    
    return count

if __name__ == "__main__":
    with open("advent06.txt") as f:
        real_input = f.read().strip()
    
    print(solve_guard_path(real_input))        # Part 1
    print(solve_guard_path(real_input, True))  # Part 2