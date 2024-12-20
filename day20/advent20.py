def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def find_start_end(grid):
    start = end = None
    for row_index, row in enumerate(grid):
        for col_index, val in enumerate(row):
            if val == 'S':
                start = (row_index, col_index)
                grid[row_index][col_index] = '.'
            elif val == 'E':
                end = (row_index, col_index)
                grid[row_index][col_index] = '.'
            if start and end:
                return start, end
    return start, end

def bfs(position, grid, rows, cols):
    distance = [[-1]*cols for _ in range(rows)]
    distance[position[0]][position[1]] = 0
    queue = [position]
    while queue:
        row, col = queue.pop(0)
        for delta_row, delta_col in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '.' and distance[new_row][new_col] == -1:
                distance[new_row][new_col] = distance[row][col] + 1
                queue.append((new_row, new_col))
    return distance

def calculate_cheats(grid, dist_start, dist_end, rows, cols, normal_time, limit):
    count = 0
    offsets = [(delta_row, delta_col) for delta_row in range(-limit, limit+1) for delta_col in range(-limit, limit+1)
               if 0 < abs(delta_row) + abs(delta_col) <= limit]
    for row_index in range(rows):
        for col_index in range(cols):
            if grid[row_index][col_index] == '.' and dist_start[row_index][col_index] != -1:
                for delta_row, delta_col in offsets:
                    new_row, new_col = row_index + delta_row, col_index + delta_col
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '.' and dist_end[new_row][new_col] != -1:
                        total = dist_start[row_index][col_index] + abs(delta_row) + abs(delta_col) + dist_end[new_row][new_col]
                        if normal_time - total >= 100:
                            count += 1
    return count

def main():
    grid = read_grid('advent20.txt')
    start, end = find_start_end(grid)
    rows, cols = len(grid), len(grid[0])
    dist_start = bfs(start, grid, rows, cols)
    dist_end = bfs(end, grid, rows, cols)
    normal = dist_start[end[0]][end[1]]
    
    part1 = calculate_cheats(grid, dist_start, dist_end, rows, cols, normal, 2)
    part2 = calculate_cheats(grid, dist_start, dist_end, rows, cols, normal, 20)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()