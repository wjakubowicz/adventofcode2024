def transform_stones(stones):
    transformed_stones = {}
    for stone, count in stones.items():
        if stone == 0:
            if 1 in transformed_stones:
                transformed_stones[1] += count
            else:
                transformed_stones[1] = count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            left_half, right_half = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
            if left_half in transformed_stones:
                transformed_stones[left_half] += count
            else:
                transformed_stones[left_half] = count
            if right_half in transformed_stones:
                transformed_stones[right_half] += count
            else:
                transformed_stones[right_half] = count
        else:
            transformed_stones[stone * 2024] = transformed_stones.get(stone * 2024, 0) + count
    return transformed_stones

def simulate_blinks(initial_stones, blink_count):
    stones = {stone: 1 for stone in initial_stones}
    for _ in range(blink_count):
        stones = transform_stones(stones)
    return stones

def main():
    with open('advent11.txt') as file:
        initial_stones = list(map(int, file.read().strip().split()))

    # Part 1: Simulate the transformation for 25 blinks
    final_stones_25 = simulate_blinks(initial_stones, 25)
    print("Number of stones after 25 blinks:", sum(final_stones_25.values()))

    # Part 2: Simulate the transformation for 75 blinks
    final_stones_75 = simulate_blinks(initial_stones, 75)
    print("Number of stones after 75 blinks:", sum(final_stones_75.values()))

if __name__ == "__main__":
    main()