def read_connections(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            computer1, computer2 = line.strip().split('-')
            graph.setdefault(computer1, set()).add(computer2)
            graph.setdefault(computer2, set()).add(computer1)
    return graph

def combinations(iterable, combination_size):
    pool = list(iterable)
    total = len(pool)
    if combination_size > total:
        return
    indices = list(range(combination_size))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(combination_size)):
            if indices[i] != i + total - combination_size:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, combination_size):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def find_cliques(graph):
    cliques = []
    def extend(current_clique, candidate_nodes):
        if not candidate_nodes and len(current_clique) >= 3:
            cliques.append(current_clique)
            return
        for node in list(candidate_nodes):
            extend(current_clique + [node], candidate_nodes & graph.get(node, set()))
            candidate_nodes.remove(node)
    extend([], set(graph))
    return cliques

def part1(graph):
    return len({tuple(sorted(nodes)) for clique in find_cliques(graph)
                for nodes in combinations(clique, 3) if any(n.startswith('t') for n in nodes)})

def part2(graph):
    return ",".join(sorted(max(find_cliques(graph), key=len)))

def main():
    graph = read_connections('advent23.txt')
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")

if __name__ == "__main__":
    main()