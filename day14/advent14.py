def read_robots(filename):
    with open(filename) as f:
        return [(*map(int, parts[0][2:].split(',')), *map(int, parts[1][2:].split(',')))
                for line in f if (parts := line.strip().split())]

def simulate_robots(robots, steps, width, height):
    return [((pos_x + steps * vel_x) % width, (pos_y + steps * vel_y) % height, vel_x, vel_y)
            for pos_x, pos_y, vel_x, vel_y in robots]

def count_quadrants(robots, mid_x, mid_y):
    counts = [0] * 4
    for pos_x, pos_y, _, _ in robots:
        if pos_x != mid_x and pos_y != mid_y:
            index = (pos_x < mid_x) * 2 + (pos_y > mid_y)
            counts[index] += 1
    return counts

def is_christmas_tree(robots, tree_positions):
    robot_positions = {(pos_x, pos_y) for pos_x, pos_y, _, _ in robots}
    return tree_positions <= robot_positions

def part1(filename, width, height):
    robots = read_robots(filename)
    robots = simulate_robots(robots, 100, width, height)
    counts = count_quadrants(robots, width // 2, height // 2)
    result = 1
    for count in counts:
        result *= count
    return result

def part2(filename, width, height):
    robots = read_robots(filename)
    mid_x, mid_y = width // 2, height // 2
    tree_offsets = [
        (0, -3),
        (-1, -2), (0, -2), (1, -2),
        (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
        (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0)
    ]
    tree_positions = {(mid_x + dx, mid_y + dy) for dx, dy in tree_offsets}
    seconds = 0
    while True:
        if is_christmas_tree(robots, tree_positions):
            return seconds
        robots = simulate_robots(robots, 1, width, height)
        seconds += 1

def main():
    width, height = 101, 103
    filename = 'advent14.txt'
    print(f"Part 1 (Safety factor after 100 seconds): {part1(filename, width, height)}")
    print(f"Part 2 (Seconds until Christmas tree pattern): {part2(filename, width, height)}")

if __name__ == "__main__":
    main()