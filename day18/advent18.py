def read_all_positions(filename):
    with open(filename, 'r') as file_handle:
        return [tuple(map(int, line.strip().split(','))) for line in file_handle if line.strip()]

def bfs(start_position, end_position, grid_size, corrupted_positions):
    node_queue = [(start_position[0], start_position[1], 0)]
    current_index = 0
    visited_positions = {(start_position[0], start_position[1])}
    while current_index < len(node_queue):
        current_x, current_y, steps = node_queue[current_index]
        current_index += 1
        if (current_x, current_y) == end_position:
            return steps
        for delta_x, delta_y in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_x, next_y = current_x + delta_x, current_y + delta_y
            if 0 <= next_x <= grid_size and 0 <= next_y <= grid_size and (next_x, next_y) not in corrupted_positions and (next_x, next_y) not in visited_positions:
                node_queue.append((next_x, next_y, steps + 1))
                visited_positions.add((next_x, next_y))
    return None

def main():
    grid_size = 70
    all_positions = read_all_positions('advent18.txt')
    corrupted_positions = set(all_positions[:1024])
    start_position, end_position = (0, 0), (70, 70)
    if start_position in corrupted_positions or end_position in corrupted_positions:
        print("Starting or ending position is corrupted.")
        return
    steps = bfs(start_position, end_position, grid_size, corrupted_positions)
    if steps is not None:
        print("Part 1:", steps)
    else:
        print("No path to exit.")
        return
    for position in all_positions[1024:]:
        corrupted_positions.add(position)
        if bfs(start_position, end_position, grid_size, corrupted_positions) is None:
            print(f"Part 2: {position[0]},{position[1]}")
            return
    print("No blocking position found.")

if __name__ == "__main__":
    main()