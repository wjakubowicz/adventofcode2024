def find_starts(tmap):
    return [(i, j) for i in range(len(tmap)) for j in range(len(tmap[0])) if tmap[i][j] == 0]

def bfs(tmap, start):
    queue = [start]
    seen = {start}
    score = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(tmap), len(tmap[0])
    
    while queue:
        x, y = queue.pop(0)
        if tmap[x][y] == 9:
            score += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and tmap[nx][ny] == tmap[x][y] + 1:
                seen.add((nx, ny))
                queue.append((nx, ny))
    return score

def dfs(tmap, x, y, seen):
    if tmap[x][y] == 9:
        return 1
    score = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(tmap), len(tmap[0])
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and tmap[nx][ny] == tmap[x][y] + 1:
            score += dfs(tmap, nx, ny, seen | {(nx, ny)})
    return score

def solve(file_path, search_func):
    with open(file_path, 'r') as file:
        tmap = [list(map(int, line.strip())) for line in file]
    starts = find_starts(tmap)
    return sum(search_func(tmap, start) for start in starts)

def main():
    file_path = "advent10.txt"
    print(f"BFS Score: {solve(file_path, bfs)}")
    print(f"DFS Rating: {solve(file_path, lambda m, s: dfs(m, s[0], s[1], {s}))}")

if __name__ == "__main__":
    main()