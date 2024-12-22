def transform(secret):
    secret = (secret ^ (secret << 6)) % 16777216
    secret = (secret ^ (secret >> 5)) % 16777216
    secret = (secret ^ (secret << 11)) % 16777216
    return secret

def part1(data):
    results = []
    for secret in map(int, data):
        for _ in range(2000):
            secret = transform(secret)
        results.append(secret)
    return sum(results)

def part2(data):
    prices = []
    for secret in map(int, data):
        price = []
        for _ in range(2000):
            secret = transform(secret)
            price.append(secret % 10)
        prices.append(price)

    changes = [[b - a for a, b in zip(p, p[1:])] for p in prices]
    amounts = {}
    for idx, change in enumerate(changes):
        keys = set()
        for i in range(len(change) - 3):
            key = tuple(change[i : i + 4])
            if key not in keys:
                if key not in amounts:
                    amounts[key] = 0
                amounts[key] += prices[idx][i + 4]
                keys.add(key)
    return max(amounts.values())

def main():
    with open('advent22.txt', 'r') as file:
        data = [line.strip() for line in file if line.strip()]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()