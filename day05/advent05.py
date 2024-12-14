def parse_input(lines):
    split = lines.index('') if '' in lines else len(lines)
    rules = [(int(a), int(b)) for a, b in (line.split('|') for line in lines[:split])]
    updates = [list(map(int, line.split(','))) for line in lines[split+1:] if line]
    return rules, updates

def is_valid(update, rules):
    pos = {page: i for i, page in enumerate(update)}
    return all(pos.get(a, -1) < pos.get(b, -1) for a, b in rules if a in pos and b in pos)

def sort_pages(pages, rules):
    graph = {a: set() for a, _ in rules if a in pages}
    for a, b in rules:
        if a in pages and b in pages:
            graph[a].add(b)
    visited, sorted_pages = set(), []
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            sorted_pages.append(node)
    for node in graph:
        dfs(node)
    return [p for p in pages if p not in visited] + sorted_pages[::-1]

def solve(lines):
    rules, updates = parse_input(lines)
    part1 = sum(u[len(u)//2] for u in updates if is_valid(u, rules))
    part2 = sum(sort_pages(u, rules)[len(u)//2] for u in updates if not is_valid(u, rules))
    return part1, part2

def main():
    with open('advent05.txt') as f:
        part1, part2 = solve(f.read().splitlines())
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()