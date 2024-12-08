import re

def part1(data):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)

def part2(data):
    enabled = True
    result = 0
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, data)
    
    for inst in instructions:
        if inst[0] == "do()":
            enabled = True
        elif inst[0] == "don't()":
            enabled = False
        else:
            if enabled:
                result += int(inst[1]) * int(inst[2])
            
    return result

if __name__ == '__main__':
    with open('advent03.txt') as f:
        data = f.read()
        print(part1(data))
        print(part2(data))