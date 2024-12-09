def decompress(disk_map: str) -> list[tuple[int, int]]: # Decompress the disk map into a list of tuples for Part 1
    return [
        (i // 2 if i % 2 == 0 else -1, 1)
        for i, d in enumerate(disk_map)
        for _ in range(int(d))
    ]

def decompress_v2(disk_map: str) -> list[tuple[int, int]]: # Decompress the disk map into a list of tuples for Part 2
    return [
        (i // 2 if i % 2 == 0 else -1, int(d))
        for i, d in enumerate(disk_map)
    ]

def compact(decompressed_map: list[tuple[int, int]]) -> None: # Compact the decompressed map in place for Part 1
    left, right = 0, len(decompressed_map) - 1

    while left < right:
        while left < right and decompressed_map[left][0] >= 0:
            left += 1
        while left < right and decompressed_map[right][0] == -1:
            right -= 1

        if left < right:
            decompressed_map[left], decompressed_map[right] = (
                decompressed_map[right],
                decompressed_map[left],
            )
            left += 1
            right -= 1

def compact_v2(decompressed_map: list[tuple[int, int]]) -> None: # Compact the decompressed map in place for Part 2
    for i in range(len(decompressed_map) - 1, -1, -1):
        for j in range(i):
            i_val, i_size = decompressed_map[i]
            j_val, j_size = decompressed_map[j]

            if i_val > 0 and j_val < 0 and i_size <= j_size:
                decompressed_map[i] = (-1, i_size)
                decompressed_map[j] = (-1, j_size - i_size)
                decompressed_map.insert(j, (i_val, i_size))
                break

def expand(decompressed_map: list[tuple[int, int]]) -> list[int]: # Expand the decompressed map into a list of integers
    return [val for val, size in decompressed_map for _ in range(size)]

def check_sum(expanded_map: list[int]) -> int: # Calculate the checksum of the expanded map
    return sum(i * c for i, c in enumerate(expanded_map) if c >= 0)

def main():
    with open("advent09.txt") as f:
        disk_map = f.read().strip()

    decompressed = decompress(disk_map)
    compact(decompressed)
    checksum1 = check_sum(expand(decompressed))
    print("Part 1:", checksum1)

    decompressed_v2 = decompress_v2(disk_map)
    compact_v2(decompressed_v2)
    checksum2 = check_sum(expand(decompressed_v2))
    print("Part 2:", checksum2)

if __name__ == "__main__":
    main()