def find_regions(grid):
    height, width = len(grid), len(grid[0])
    visited = set()
    regions = []

    def explore_region(row, col, letter):
        if (row, col) in visited or row < 0 or col < 0 or row >= height or col >= width or grid[row][col] != letter:
            return set()
        
        visited.add((row, col))
        coords = {(row, col)}
        
        for delta_row, delta_col in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            coords.update(explore_region(row + delta_row, col + delta_col, letter))
            
        return coords
    
    for row in range(height):
        for col in range(width):
            if (row, col) not in visited:
                region = explore_region(row, col, grid[row][col])
                if region:
                    regions.append(region)
                    
    return regions

def calculate_perimeter(region):
    perimeter = 0
    for row, col in region:
        for delta_row, delta_col in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (row + delta_row, col + delta_col) not in region:
                perimeter += 1
                
    return perimeter

def parse_data(input_data):
    grid = [list(line.strip()) for line in input_data.strip().splitlines()]
    coords_by_plant = {}
    for row, grid_row in enumerate(grid):
        for col, cell in enumerate(grid_row):
            if cell not in coords_by_plant:
                coords_by_plant[cell] = set()
            coords_by_plant[cell].add((row, col))
    return grid, coords_by_plant

def get_group_sides(group):
    min_row = min(group, key=lambda x: x[0])[0]
    max_row = max(group, key=lambda x: x[0])[0]
    min_col = min(group, key=lambda x: x[1])[1]
    max_col = max(group, key=lambda x: x[1])[1]
    rows = max_row - min_row + 1
    cols = max_col - min_col + 1
    normalized_group = [(row - min_row, col - min_col) for row, col in group]

    grid = [[" " for _ in range(cols + 2)] for _ in range(rows + 2)]
    for row, col in normalized_group:
        grid[row + 1][col + 1] = "X"

    sides = 0
    for _ in range(2):
        for row in range(1, rows + 1):
            sides += len("".join(["X" if current != above and current == "X" else " " 
                                for current, above in zip(grid[row], grid[row - 1])]).split())
            sides += len("".join(["X" if current != above and current == "X" else " " 
                                for current, above in zip(grid[row], grid[row + 1])]).split())

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
        row, col = stack.pop()
        if (row, col) in visited or row < 0 or col < 0 or row >= height or col >= width or grid[row][col] != letter:
            continue
        visited.add((row, col))
        group.add((row, col))
        for delta_row, delta_col in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            stack.append((row + delta_row, col + delta_col))

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
    grid, coords_by_plant = parse_data(input_data)
    plant_types = set(coords_by_plant.keys())
    prices = {}

    for plant_type in plant_types:
        prices[plant_type] = 0
        coords = coords_by_plant[plant_type]

        while coords:
            coord = coords.pop()
            curr_group = get_curr_group(grid, coord)
            coords -= curr_group

            group_sides = get_group_sides(curr_group)
            price = len(curr_group) * group_sides
            prices[plant_type] += price

    return sum(prices.values())

def main():
    with open('advent12.txt', 'r') as f:
        input_data = f.read()
    result_part1 = solve_part1(input_data)
    print(f"Total price of fencing (Part 1): {result_part1}")
    result_part2 = solve_part2(input_data)
    print(f"Total price of fencing (Part 2): {result_part2}")

if __name__ == '__main__':
    main()