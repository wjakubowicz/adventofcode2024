DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

def get_robot_pos(grid):
    return next((row, col) for row, row_vals in enumerate(grid) for col, val in enumerate(row_vals) if val == "@")

def get_adjs_and_edges_p1(grid, pos, move):
    row, col = pos
    delta_row, delta_col = DIRS[move]
    adjacents = set()
    while True:
        row += delta_row
        col += delta_col
        if grid[row][col] in ".#":
            return [(row - delta_row, col - delta_col)], adjacents
        adjacents.add((row, col))

def get_adjs_and_edges_p2(grid, pos, move):
    row, col = pos
    delta_row, delta_col = DIRS[move]
    edges = []
    adjacents = set()
    queue = [pos]
    while queue:
        row, col = queue.pop(0)
        if (row, col) in adjacents:
            continue
        adjacents.add((row, col))
        next_row, next_col = row + delta_row, col + delta_col
        cell = grid[next_row][next_col]
        if cell in ".#":
            edges.append((row, col))
        elif cell == "[":
            queue.extend([(next_row, next_col), (next_row, next_col + 1)])
        elif cell == "]":
            queue.extend([(next_row, next_col), (next_row, next_col - 1)])
    return edges, adjacents - {pos}

def update_grid(grid, adjacents, move):
    delta_row, delta_col = DIRS[move]
    sorted_coords = sorted(adjacents, key=lambda x: (x[0], x[1]), reverse=move in ("v", ">"))
    for row, col in sorted_coords:
        grid[row + delta_row][col + delta_col], grid[row][col] = grid[row][col], "."
    return grid

def moving_p1(grid, pos, moves):
    for move in moves:
        delta_row, delta_col = DIRS[move]
        next_row, next_col = pos[0] + delta_row, pos[1] + delta_col
        cell = grid[next_row][next_col]
        if cell == ".":
            pos = (next_row, next_col)
        elif cell != "#":
            edges, adjs = get_adjs_and_edges_p1(grid, pos, move)
            if not sum(1 for b in edges if grid[b[0]+delta_row][b[1]+delta_col] == "#"):
                grid = update_grid(grid, adjs, move)
                pos = (next_row, next_col)
    return grid

def moving_p2(grid, pos, moves):
    for move in moves:
        delta_row, delta_col = DIRS[move]
        next_row, next_col = pos[0] + delta_row, pos[1] + delta_col
        cell = grid[next_row][next_col]
        if cell == ".":
            pos = (next_row, next_col)
        elif cell != "#":
            edges, adjs = get_adjs_and_edges_p2(grid, pos, move)
            if not sum(1 for b in edges if grid[b[0]+delta_row][b[1]+delta_col] == "#"):
                grid = update_grid(grid, adjs, move)
                pos = (next_row, next_col)
    return grid

def get_coords_sum_p1(grid):
    return sum(100 * row + col for row, row_vals in enumerate(grid) for col, val in enumerate(row_vals) if val == "O")

def get_coords_sum_p2(grid):
    return sum(100 * row + col for row, row_vals in enumerate(grid) for col, val in enumerate(row_vals) if val == "[")

def resize_grid(grid):
    mappings = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    return [list("".join(mappings.get(char, char) for char in row)) for row in grid]

def parse_input(data):
    grid_text, moves_text = "\n".join(data).split("\n\n")
    grid = [list(row) for row in grid_text.split("\n")]
    moves = list(moves_text.replace("\n", ""))
    return grid, moves

def part1(data):
    grid, moves = parse_input(data)
    pos = get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."
    grid = moving_p1(grid, pos, moves)
    return get_coords_sum_p1(grid)

def part2(data):
    grid, moves = parse_input(data)
    grid = resize_grid(grid)
    pos = get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."
    grid = moving_p2(grid, pos, moves)
    return get_coords_sum_p2(grid)

def main():
    with open("advent15.txt") as f:
        data = f.read().splitlines()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()