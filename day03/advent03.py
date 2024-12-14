def parse_mul_instruction(memory, index): # Parse a valid mul(X,Y) instruction and return the product
    index += 4
    num1 = num2 = ''
    
    while index < len(memory) and memory[index].isdigit():
        num1 += memory[index]
        index += 1
    
    if index < len(memory) and memory[index] == ',':
        index += 1
        while index < len(memory) and memory[index].isdigit():
            num2 += memory[index]
            index += 1
        if index < len(memory) and memory[index] == ')':
            return index + 1, int(num1) * int(num2)
    
    return index, 0

def sum_valid_multiplications(memory): # Sum results of all valid mul(X,Y) instructions in corrupted memory
    total, index = 0, 0
    while index < len(memory):
        if memory.startswith('mul(', index):
            index, product = parse_mul_instruction(memory, index)
            total += product
        else:
            index += 1
            
    return total

def sum_enabled_multiplications(memory): # Sum results of enabled mul(X,Y) instructions, respecting do() and don't()
    total, index, multiplication_enabled = 0, 0, True
    
    while index < len(memory):
        if memory.startswith('do()', index):
            multiplication_enabled, index = True, index + 4
        elif memory.startswith("don't()", index):
            multiplication_enabled, index = False, index + 7
        elif memory.startswith('mul(', index):
            index, product = parse_mul_instruction(memory, index)
            if multiplication_enabled:
                total += product
        else:
            index += 1
    
    return total

def main():
    with open('advent03.txt') as f:
        corrupted_memory = f.read()
        print(f"Part 1: {sum_valid_multiplications(corrupted_memory)}")
        print(f"Part 2: {sum_enabled_multiplications(corrupted_memory)}")

if __name__ == '__main__':
    main()