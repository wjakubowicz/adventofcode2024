def parse_input(file_path, adjust_prize=False):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    claw_machines = []
    for i in range(0, len(lines), 4):
        machine = [tuple(int(num[2:]) for num in lines[i+j].split(': ')[1].split(', ')) for j in range(3)]
        if adjust_prize:
            machine[2] = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)
        claw_machines.append(machine)
    return claw_machines

def calculate_prizes_and_tokens(file_path, adjust_prize=False):
    claw_machines = parse_input(file_path, adjust_prize)
    total_prizes_won, total_tokens_spent = 0, 0
    for machine in claw_machines:
        tokens_needed = compute_tokens_needed(*machine[0], *machine[1], *machine[2])
        if tokens_needed is not None:
            total_tokens_spent += tokens_needed
            total_prizes_won += 1
    return total_prizes_won, total_tokens_spent

def compute_tokens_needed(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    determinant = button_a_x * button_b_y - button_a_y * button_b_x
    if determinant == 0:
        return None
    t_numerator = prize_x * button_b_y - button_b_x * prize_y
    s_numerator = button_a_x * prize_y - button_a_y * prize_x
    if t_numerator % determinant != 0 or s_numerator % determinant != 0:
        return None
    t = t_numerator // determinant
    s = s_numerator // determinant
    if t < 0 or s < 0:
        return None
    return t * 3 + s
	
def main():
    file_path = 'advent13.txt'
    prizes1, tokens1 = calculate_prizes_and_tokens(file_path)
    prizes2, tokens2 = calculate_prizes_and_tokens(file_path, adjust_prize=True)
    
    print(f"Part 1 - Prizes won: {prizes1}")
    print(f"Part 1 - Total tokens spent: {tokens1}")
    print(f"Part 2 - Prizes won: {prizes2}")
    print(f"Part 2 - Total tokens spent: {tokens2}")

if __name__ == "__main__":
    main()