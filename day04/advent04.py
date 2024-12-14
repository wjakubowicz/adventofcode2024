def count_word_occurrences(grid, word="XMAS"):
    num_rows, num_cols = len(grid), len(grid[0])
    directions = [(delta_row, delta_col) for delta_row in (-1, 0, 1) 
                  for delta_col in (-1, 0, 1) if not (delta_row == delta_col == 0)]
    word_length = len(word)
    occurrence_count = sum(
        1
        for row in range(num_rows)
        for col in range(num_cols)
        if grid[row][col] == word[0]
        for delta_row, delta_col in directions
        if 0 <= row + delta_row * (word_length - 1) < num_rows 
           and 0 <= col + delta_col * (word_length - 1) < num_cols
        if all(grid[row + delta_row * i][col + delta_col * i] == word[i] 
               for i in range(word_length))
    )
    return occurrence_count

def count_xmas_patterns(grid):
    num_rows, num_cols = len(grid), len(grid[0])
    def is_valid_pattern(row, col, delta_row, delta_col):
        return (0 <= row - delta_row < num_rows and 0 <= col - delta_col < num_cols and
                0 <= row + delta_row < num_rows and 0 <= col + delta_col < num_cols and
                grid[row][col] == 'A' and
                ((grid[row - delta_row][col - delta_col] == 'M' and grid[row + delta_row][col + delta_col] == 'S') or
                 (grid[row - delta_row][col - delta_col] == 'S' and grid[row + delta_row][col + delta_col] == 'M'))
               )
    direction_pairs = [(1, 1), (1, -1)]
    pattern_count = sum(
        1
        for row in range(num_rows)
        for col in range(num_cols)
        if all(is_valid_pattern(row, col, delta_row, delta_col) 
               for delta_row, delta_col in direction_pairs)
    )
    return pattern_count

def main():
    with open("advent04.txt") as file:
        grid = file.read().splitlines()
    print(f"Part 1: {count_word_occurrences(grid)}")
    print(f"Part 2: {count_xmas_patterns(grid)}")

if __name__ == "__main__":
    main()