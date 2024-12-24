def read_input(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def process(op, op1, op2):
    return {"AND": op1 & op2, "OR": op1 | op2, "XOR": op1 ^ op2}[op]

def convert_to_decimal(wire_values):
    binary = ''.join(str(wire_values[k]) for k in sorted(wire_values) if k.startswith("z"))
    return int(binary, 2) if binary else 0

def parse_lines(lines):
    wires, operations, highest_z = {}, [], "z00"
    for line in lines:
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            op1, op, op2, _, res = line.split()
            operations.append((op1, op, op2, res))
            if res.startswith("z") and int(res[1:]) > int(highest_z[1:]):
                highest_z = res
    return wires, operations, highest_z

def determine_wrong_operations(operations, highest_z):
    wrong = set()
    for op1, op, op2, res in operations:
        if res.startswith("z") and op != "XOR" and res != highest_z:
            wrong.add(res)
        if op == "XOR" and not any(x.startswith(("x", "y", "z") ) for x in [res, op1, op2]):
            wrong.add(res)
        if op == "AND" and "x00" not in [op1, op2]:
            wrong.update(subres for subop1, subop, subop2, subres in operations if res in (subop1, subop2) and subop != "OR")
        if op == "XOR":
            wrong.update(subres for subop1, subop, subop2, subres in operations if res in (subop1, subop2) and subop == "OR")
    return wrong

def execute_operations(wires, operations):
    while operations:
        op1, op, op2, res = operations.pop(0)
        if op1 in wires and op2 in wires:
            wires[res] = process(op, wires[op1], wires[op2])
        else:
            operations.append((op1, op, op2, res))
    return wires

def main():
    lines = read_input("advent24.txt")
    wires, operations, highest_z = parse_lines(lines)
    wrong = determine_wrong_operations(operations, highest_z)
    wires = execute_operations(wires, operations)
    bits = convert_to_decimal(wires)
    print(f"Part 1: {bits}")
    print(f"Part 2: {','.join(sorted(wrong))}")

if __name__ == "__main__":
    main()