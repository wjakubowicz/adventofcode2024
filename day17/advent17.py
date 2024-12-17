def read_input(filename):
    return [line.strip() for line in open(filename)]

def run_program(registers, program):
    A, B, C = registers
    outputs, ptr = [], 0
    while ptr < len(program):
        opcode, operand = program[ptr], program[ptr + 1]
        v = operand if operand < 4 else [A, B, C][operand - 4]
        if opcode == 0:
            A //= 2 ** v
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = v % 8
        elif opcode == 3 and A != 0:
            ptr = operand
            continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            outputs.append(v % 8)
        elif opcode == 6:
            B = A // (2 ** v)
        elif opcode == 7:
            C = A // (2 ** v)
        ptr += 2
    return outputs

def part1(data):
    registers = [int(line.split(": ")[1]) for line in data[:3]]
    program = list(map(int, data[4].split(": ")[1].split(",")))
    return ",".join(map(str, run_program(registers, program)))

def part2(data):
    program = list(map(int, data[4].split(": ")[1].split(",")))
    A = sum(7 * 8 ** i for i in range(len(program) - 1)) + 1
    while True:
        result = run_program([A, 0, 0], program)
        if result == program:
            return A
        for i in reversed(range(len(result))):
            if result[i] != program[i]:
                A += 8 ** i
                break

def main():
    data = read_input('advent17.txt')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()