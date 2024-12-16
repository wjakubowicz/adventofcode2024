def read_maze(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def is_valid(grid, row_index, col_index):
    return (0 <= row_index < len(grid) and 0 <= col_index < len(grid[0]) and grid[row_index][col_index] != '#')

def find_routes(grid):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    start = end = None
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 'S':
                start = (row_index, col_index)
            elif cell == 'E':
                end = (row_index, col_index)
    routes = []
    visited = {}
    queue = [(start, [start], 0, 0)]  # (row, col), history, score, direction_index
    while queue:
        (row_index, col_index), history, current_score, current_direction = queue.pop(0)
        if (row_index, col_index) == end:
            routes.append((history, current_score))
            continue
        if ((row_index, col_index), current_direction) in visited and visited[((row_index, col_index), current_direction)] < current_score:
            continue
        visited[((row_index, col_index), current_direction)] = current_score
        for direction_index, (delta_row, delta_col) in enumerate(directions):
            if (current_direction + 2) % 4 == direction_index:
                continue
            new_row, new_col = row_index + delta_row, col_index + delta_col
            if is_valid(grid, new_row, new_col) and (new_row, new_col) not in history:
                if direction_index == current_direction:
                    queue.append(((new_row, new_col), history + [(new_row, new_col)], current_score + 1, direction_index))  # move forward
                else:
                    queue.append(((row_index, col_index), history, current_score + 1000, direction_index))  # turn
    return routes

def part1(grid):
    possible_routes = find_routes(grid)
    min_score = min(r[1] for r in possible_routes)
    return min_score

def part2(grid):
    possible_routes = find_routes(grid)
    min_score = min(r[1] for r in possible_routes)
    best_routes = [r for r in possible_routes if r[1] == min_score]
    tiles = {tile for route in best_routes for tile in route[0]}
    return len(tiles)

def main():
    grid = read_maze('advent16.txt')
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

if __name__ == '__main__':
    main()