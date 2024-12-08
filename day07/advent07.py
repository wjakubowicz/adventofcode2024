def parse_input(input_text):
    for line in input_text.strip().split('\n'):
        val, nums = line.split(': ')
        yield int(val), list(map(int, nums.split()))

def generate_combinations(ops, length):
    if length == 0:
        yield []
    else:
        for op in ops:
            for combo in generate_combinations(ops, length - 1):
                yield [op] + combo

def solve_part1(input_text, include_concat=False):
    total = 0
    ops = '+*||' if include_concat else '+*'
    
    for test, nums in parse_input(input_text):
        for ops_combo in generate_combinations(ops, len(nums) - 1):
            try:
                result = nums[0]
                for i, op in enumerate(ops_combo):
                    result = eval(f"{result}{op}{nums[i + 1]}") if op != '||' else int(str(result) + str(nums[i + 1]))
                if result == test:
                    total += test
                    break
            except: continue
    return total

def solve_part2(input_text):
    result = 0
    for test, nums in parse_input(input_text):
        possible = {nums.pop(0)}
        while nums:
            n = nums.pop(0)
            possible = {x for p in possible for x in (p + n, p * n, int(str(p) + str(n))) if x <= test}
        if test in possible: result += test
    return result

if __name__ == '__main__':
    with open('advent07.txt') as f:
        data = f.read()
        print(f"Part 1: {solve_part1(data)}")
        print(f"Part 2: {solve_part2(data)}")