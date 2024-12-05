from typing import List, Tuple
from collections import defaultdict

def solve(lines: List[str]) -> Tuple[int, int]:
    split_idx = lines.index('\n') if '\n' in lines else lines.index('')
    rules = [(int(b), int(a)) for b, a in [l.strip().split('|') for l in lines[:split_idx]]]
    updates = [[int(x) for x in l.strip().split(',')] for l in lines[split_idx+1:] if l.strip()]
    
    def is_valid(nums: List[int]) -> bool:
        pos = {n: i for i, n in enumerate(nums)}
        return all(pos.get(b, -1) < pos.get(a, -1) for b, a in rules if b in pos and a in pos)
    
    def sort_nums(nums: List[int]) -> List[int]:
        graph = defaultdict(set)
        for b, a in rules:
            if b in nums and a in nums:
                graph[b].add(a)
        
        visited, result = set(), []
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
                result.append(node)
                
        for n in set.union(*[{b, a} for b, a in rules if b in nums and a in nums]):
            dfs(n)
            
        return [x for x in nums if x not in visited] + result[::-1]
    
    return (
        sum(u[len(u)//2] for u in updates if is_valid(u)),
        sum(sort_nums(u)[len(u)//2] for u in updates if not is_valid(u))
    )

if __name__ == '__main__':
    with open('advent05.txt') as f:
        p1, p2 = solve(f.readlines())
        print(f"Part 1: {p1}\nPart 2: {p2}")