def find_interference(antenna_data, check_path=False):
    antenna_grid = [line.strip() for line in antenna_data]
    rows, cols = len(antenna_grid), len(antenna_grid[0])
    frequency_map = {}
    for row, line in enumerate(antenna_grid):
        for col, symbol in enumerate(line):
            if symbol != '.':
                frequency_map.setdefault(symbol, []).append((row, col))
    antinodes = set()
    for antenna_positions in frequency_map.values():
        if len(antenna_positions) > 1:
            if check_path:
                antinodes.update(antenna_positions)
            for i, (row1, col1) in enumerate(antenna_positions):
                for row2, col2 in antenna_positions[i+1:]:
                    delta_row, delta_col = row2 - row1, col2 - col1
                    for base_row, base_col, direction_multiplier in [(row1, col1, -1), (row2, col2, 1)]:
                        current_row, current_col = base_row + delta_row * direction_multiplier, base_col + delta_col * direction_multiplier
                        if check_path:
                            while 0 <= current_row < rows and 0 <= current_col < cols:
                                antinodes.add((current_row, current_col))
                                current_row += delta_row * direction_multiplier
                                current_col += delta_col * direction_multiplier
                        else:
                            if 0 <= current_row < rows and 0 <= current_col < cols:
                                antinodes.add((current_row, current_col))
    return len(antinodes)

def main():
    with open('advent08.txt') as f:
        antenna_data = f.readlines()
    part_one_result = find_interference(antenna_data)
    part_two_result = find_interference(antenna_data, True)
    print(f"Part 1 - Number of interference points: {part_one_result}")
    print(f"Part 2 - Number of antinodes: {part_two_result}")

if __name__ == "__main__":
    main()