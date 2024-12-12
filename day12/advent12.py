def find_regions(grid):
    height, width = len(grid), len(grid[0])
    visited = set()
    regions = []

    def explore_region(r, c, letter):
        if (r, c) in visited or r < 0 or c < 0 or r >= height or c >= width or grid[r][c] != letter:
            return set()
        
        visited.add((r, c))
        coords = {(r, c)}
        
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            coords.update(explore_region(r + dr, c + dc, letter))
            
        return coords
    
    for r in range(height):
        for c in range(width):
            if (r, c) not in visited:
                region = explore_region(r, c, grid[r][c])
                if region:
                    regions.append(region)
                    
    return regions

def calculate_perimeter(region):
    perimeter = 0
    for r, c in region:
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (r + dr, c + dc) not in region:
                perimeter += 1
                
    return perimeter

def parse_data(input_data):
    grid = [list(line.strip()) for line in input_data.strip().splitlines()]
    coords_by_type = {}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell not in coords_by_type:
                coords_by_type[cell] = set()
            coords_by_type[cell].add((r, c))
    return grid, coords_by_type

def get_group_sides(group):
    min_y = min(group, key=lambda x: x[0])[0]
    max_y = max(group, key=lambda x: x[0])[0]
    min_x = min(group, key=lambda x: x[1])[1]
    max_x = max(group, key=lambda x: x[1])[1]
    rows = max_y - min_y + 1
    cols = max_x - min_x + 1
    new_group = [(y - min_y, x - min_x) for y, x in group]

    grid = [[" " for _ in range(cols + 2)] for _ in range(rows + 2)]
    for y, x in new_group:
        grid[y + 1][x + 1] = "X"

    sides = 0

    for _ in range(2):
        for y in range(1, rows + 1):
            sides += len("".join(["X" if current != above and current == "X" else " " for current, above in zip(grid[y], grid[y - 1])]).split())
            sides += len("".join(["X" if current != above and current == "X" else " " for current, above in zip(grid[y], grid[y + 1])]).split())

        grid = list(zip(*grid[::-1]))
        rows, cols = cols, rows

    return sides

def get_curr_group(grid, start):
    height, width = len(grid), len(grid[0])
    letter = grid[start[0]][start[1]]
    visited = set()
    stack = [start]
    group = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in visited or r < 0 or c < 0 or r >= height or c >= width or grid[r][c] != letter:
            continue
        visited.add((r, c))
        group.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            stack.append((r + dr, c + dc))

    return group

def solve_part1(input_data):
    grid = [list(line.strip()) for line in input_data.strip().splitlines()]
    total_price = 0
    regions = find_regions(grid)
    
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region)
        price = area * perimeter
        total_price += price
        
    return total_price

def solve_part2(input_data):
    grid, coords_by_type = parse_data(input_data)
    types = set(coords_by_type.keys())
    prices = {}

    for _type in types:
        prices[_type] = 0
        coords = coords_by_type[_type]

        while coords:
            coord = coords.pop()
            curr_group = get_curr_group(grid, coord)
            coords -= curr_group

            group_sides = get_group_sides(curr_group)
            price = len(curr_group) * group_sides
            prices[_type] += price

    return sum(prices.values())

# Read input from file
with open('advent12.txt', 'r') as f:
    input_data = f.read()

result_part1 = solve_part1(input_data)
print(f"Total price of fencing (Part 1): {result_part1}")

result_part2 = solve_part2(input_data)
print(f"Total price of fencing (Part 2): {result_part2}")