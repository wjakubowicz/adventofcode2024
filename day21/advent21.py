def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def arrow_str(delta_x, delta_y):
    return ("<"*max(0, -delta_x) + "^"*max(0, -delta_y) + "v"*max(0, delta_y) + ">"*max(0, delta_x))

def keypad(use_first_option, positions_map, code_string, current_x, current_y):
    moves = []
    for c in code_string:
        cx, cy = positions_map[c]
        delta_x, delta_y = cx - current_x, cy - current_y
        if use_first_option:
            if delta_x == 2 and delta_y > 0 and cy == 3:
                moves.append(">"*delta_x + "v"*delta_y)
            elif delta_x == -2 and delta_y < 0 and current_y == 3:
                moves.append("^"*abs(delta_y) + "<<")
            elif delta_x == -1 and current_x == 1 and delta_y < 0 and current_y == 3:
                moves.append("^"*abs(delta_y) + "<")
            else:
                moves.append(arrow_str(delta_x, delta_y))
        else:
            if (delta_x, delta_y) == (2, -1):
                moves.append(">>^")
            elif (delta_x, delta_y) == (-2, 1):
                moves.append("v<<")
            elif delta_x == -1 and delta_y == 1 and current_x == 1 and current_y == 0:
                moves.append("v<")
            elif delta_x == 1 and delta_y == -1 and current_x == 0 and current_y == 1:
                moves.append(">^")
            else:
                moves.append(arrow_str(delta_x, delta_y))
        moves.append("A")
        current_x, current_y = cx, cy
    return "".join(moves)

def parse_segments(sequence, increment=1):
    result = {}
    seg = ""
    for ch in sequence:
        seg += ch
        if ch == "A":
            result[seg] = result.get(seg, 0) + increment
            seg = ""
    return result

def breakCode(code_string):
    return parse_segments(code_string)

def keycounts(use_first_option, positions_map, code_map, current_x, current_y):
    new_map = {}
    for code_segment, frequency in code_map.items():
        partial = parse_segments(keypad(use_first_option, positions_map, code_segment, current_x, current_y), frequency)
        for seg, val in partial.items():
            new_map[seg] = new_map.get(seg, 0) + val
    return new_map

def complexity(count_map):
    return sum(len(k)*v for k, v in count_map.items())

def main():
    numPos = {"7":(0,0),"8":(1,0),"9":(2,0),"4":(0,1),"5":(1,1),"6":(2,1), "1":(0,2),"2":(1,2),"3":(2,2),"0":(1,3),"A":(2,3)}
    dirPos = {"^":(1,0),"A":(2,0),"<":(0,1),"v":(1,1),">":(2,1)}
    total_part1 = 0
    total_part2 = 0
    with open("advent21.txt") as f:
        for line in f:
            line = line.strip()
            code_map = parse_segments(line)
            previous_map = keycounts(True, numPos, code_map, 2, 3)
            for iteration in range(25):
                previous_map = keycounts(False, dirPos, previous_map, 2, 0)
                if iteration == 1:
                    total_part1 += complexity(previous_map) * int(line[:3])
            total_part2 += complexity(previous_map) * int(line[:3])
    print(f"Part 1: {total_part1}")
    print(f"Part 2: {total_part2}")

if __name__ == "__main__":
    main()