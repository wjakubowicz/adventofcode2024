from typing import List, Tuple
from collections import defaultdict

def solve(lines: List[str]) -> Tuple[int, int]:
    split_idx = lines.index('\n') if '\n' in lines else lines.index('') # Find the index where the rules and updates are separated
    rules = [(int(b), int(a)) for b, a in [l.strip().split('|') for l in lines[:split_idx]]] # Parse the rules from the input lines
    updates = [[int(x) for x in l.strip().split(',')] for l in lines[split_idx+1:] if l.strip()] # Parse the updates from the input lines
    
    def is_valid(nums: List[int]) -> bool: # Check if a list of numbers is valid according to the rules
        pos = {n: i for i, n in enumerate(nums)}
        return all(pos.get(b, -1) < pos.get(a, -1) for b, a in rules if b in pos and a in pos)
    
    def sort_nums(nums: List[int]) -> List[int]: # Sort a list of numbers according to the rules
        graph = defaultdict(set)
        for b, a in rules:
            if b in nums and a in nums:
                graph[b].add(a)
        
        visited, result = set(), []
        
        def dfs(node): # Depth-first search to sort the numbers
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
                result.append(node)
                
        for n in set.union(*[{b, a} for b, a in rules if b in nums and a in nums]): # Perform DFS for each node in the graph
            dfs(n)
            
        return [x for x in nums if x not in visited] + result[::-1] # Return the sorted list of numbers
    
    part1_result = sum(u[len(u)//2] for u in updates if is_valid(u))
    part2_result = sum(sort_nums(u)[len(u)//2] for u in updates if not is_valid(u))
    return part1_result, part2_result

if __name__ == '__main__':
    with open('advent05.txt') as file:
        lines = file.readlines()
        part1, part2 = solve(lines)
        print(f"Part 1: {part1}\nPart 2: {part2}")