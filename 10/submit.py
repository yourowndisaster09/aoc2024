import sys
from collections import deque

def part1(topomap):
    m = len(topomap)
    n = len(topomap[0])

    score = 0
    for i in range(m):
        for j in range(n):
            if topomap[i][j] == 0:
                visited = [[False for _ in range(n)] for _ in range(m)]
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    if visited[x][y]:
                        continue
                    if topomap[x][y] == 9:
                        score += 1
                    visited[x][y] = True
                    nextPaths = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for r, c in nextPaths:
                        if r > -1 and r < m and c > -1 and c < n and not visited[r][c] and topomap[r][c] == topomap[x][y] + 1:
                            q.append((r, c))
    return score
                    

def part2(topomap):
    m = len(topomap)
    n = len(topomap[0])

    def countPaths(i, j, num):
        if topomap[i][j] == 9:
            return 1
        nextPaths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        count = 0
        for r, c in nextPaths:
            if r > -1 and r < m and c > -1 and c < n and topomap[r][c] == num + 1:
                count += countPaths(r, c, num + 1)
        return count
        
    score = 0
    for i in range(m):
        for j in range(n):
            if topomap[i][j] == 0:
                score += countPaths(i, j, 0)
    return score


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            data.append([int(x) for x in l])

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')