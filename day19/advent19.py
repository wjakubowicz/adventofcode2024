def is_valid_pattern(text, patterns, memo):
    if text in memo: return memo[text]
    if not text: return True
    
    for pattern in patterns:
        if text.startswith(pattern):
            if is_valid_pattern(text[len(pattern):], patterns, memo):
                memo[text] = True
                return True
    
    memo[text] = False
    return False

def count_combinations(text, patterns, memo):
    if text in memo: return memo[text]
    if not text: return 1
    
    result = 0
    for pattern in patterns:
        if text.startswith(pattern):
            result += count_combinations(text[len(pattern):], patterns, memo)
    
    memo[text] = result
    return result

def solve_part1(designs, patterns):
    memo = {}
    return sum(is_valid_pattern(d, patterns, memo) for d in designs)

def solve_part2(designs, patterns):
    memo = {}
    return sum(count_combinations(d, patterns, memo) for d in designs)

def main():
    with open('advent19.txt') as f:
        patterns, designs = f.read().strip().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.splitlines()
    
    print(f"Part 1: {solve_part1(designs, patterns)}")
    print(f"Part 2: {solve_part2(designs, patterns)}")

if __name__ == "__main__":
    main()