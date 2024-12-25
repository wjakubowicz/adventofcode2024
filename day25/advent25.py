def parse(data):
	with open("advent25.txt") as f:
		return f.read().strip().split('\n')

def part1(data):
    locks, keys = [], []
    for block in "\n".join(data).split("\n\n"):
        rows = block.split("\n")
        pins = [sum(1 for r in rows if r[i] == "#") - 1 for i in range(len(rows[0]))]
        (locks if rows[0].count("#") == 5 else keys).append(pins)
    
    return sum(all(l + k <= 5 for l, k in zip(lock, key))
              for lock in locks for key in keys)

def part2(data):
    return "Ho Ho Ho"

def main():
	data = parse("advent25.txt")
	print(f"Part 1: {part1(data)}")

if __name__ == "__main__":
	main()