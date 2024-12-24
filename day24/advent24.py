def read_input(filename):
    with open(filename, "r") as file_obj:
        return [line.strip() for line in file_obj if line.strip()]

def process(gate_type, value_a, value_b):
    return {'AND': value_a & value_b, 'OR': value_a | value_b, 'XOR': value_a ^ value_b}.get(gate_type, 0)

def parse_and_validate(lines):
    wires, operations, highest_z, wrong = {}, [], "z00", set()
    for line_text in lines:
        if ":" in line_text:
            wire_name, wire_value = line_text.split(": ")
            wires[wire_name] = int(wire_value)
        else:
            operand1, gate_type, operand2, _, result_wire = line_text.split()
            operations.append((operand1, gate_type, operand2, result_wire))
            if result_wire.startswith("z") and int(result_wire[1:]) > int(highest_z[1:]):
                highest_z = result_wire
    for operand1, gate_type, operand2, result_wire in operations:
        if result_wire.startswith("z") and gate_type != "XOR" and result_wire != highest_z:
            wrong.add(result_wire)
        if gate_type == "XOR" and result_wire[0] not in "xyz" and operand1[0] not in "xyz" and operand2[0] not in "xyz":
            wrong.add(result_wire)
        if gate_type == "AND" and "x00" not in [operand1, operand2]:
            for sub_operand1, sub_gate_type, sub_operand2, sub_result_wire in operations:
                if result_wire in [sub_operand1, sub_operand2] and sub_gate_type != "OR":
                    wrong.add(result_wire)
        if gate_type == "XOR":
            for sub_operand1, sub_gate_type, sub_operand2, sub_result_wire in operations:
                if result_wire in [sub_operand1, sub_operand2] and sub_gate_type == "OR":
                    wrong.add(result_wire)
    return wires, operations, highest_z, wrong

def execute_ops(wires, operations):
    while operations:
        operand1, gate_type, operand2, result_wire = operations.pop(0)
        if operand1 in wires and operand2 in wires:
            wires[result_wire] = process(gate_type, wires[operand1], wires[operand2])
        else:
            operations.append((operand1, gate_type, operand2, result_wire))
    return wires

def convert_to_decimal(wires):
    zws = sorted([k for k in wires if k.startswith("z")], key=lambda x: int(x[1:]), reverse=True)
    bs = ''.join(str(wires[k]) for k in zws)
    return int(bs, 2) if bs else 0

def main():
    lines = read_input("advent24.txt")
    wires, operations, highest_z, wrong = parse_and_validate(lines)
    wires = execute_ops(wires, operations)
    print(f"Part 1: {convert_to_decimal(wires)}")
    print(f"Part 2: {','.join(sorted(wrong))}")

if __name__ == "__main__":
    main()