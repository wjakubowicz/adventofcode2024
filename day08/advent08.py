def find_interference(data, check_path=False):
    grid = [line.strip() for line in data]
    rows, cols = len(grid), len(grid[0])
    
    # Group positions by symbol
    symbols = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                symbols.setdefault(grid[r][c], []).append((r, c))

    interference = set()
    
    for positions in symbols.values():
        if len(positions) > 1:
            if check_path:
                interference.update(positions)  # Add antenna positions for part2
                
            for i, (r1, c1) in enumerate(positions):
                for r2, c2 in positions[i+1:]:
                    dr, dc = r2-r1, c2-c1
                    
                    for base_r, base_c, direction in [(r1,c1,-1), (r2,c2,1)]:
                        curr_r, curr_c = base_r, base_c
                        
                        if check_path:
                            while 0 <= curr_r < rows and 0 <= curr_c < cols:
                                interference.add((curr_r, curr_c))
                                curr_r += dr * direction
                                curr_c += dc * direction
                        else:
                            curr_r += dr * direction
                            curr_c += dc * direction
                            if 0 <= curr_r < rows and 0 <= curr_c < cols:
                                interference.add((curr_r, curr_c))

    return len(interference)

if __name__ == "__main__":
    with open('advent08.txt') as f:
        data = f.readlines()
    
    print(f"Part 1 - Number of interference points: {find_interference(data)}")
    print(f"Part 2 - Number of antinodes: {find_interference(data, True)}")