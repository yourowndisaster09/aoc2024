import sys
from collections import deque


def part1(grid):
    [print(row) for row in grid]
    print()
    m = len(grid)
    n = len(grid[0])

    q = deque()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '^':
                q.append((r, c, -1, 0))
            elif grid[r][c] == '>':
                q.append((r, c, 0, 1))
            elif grid[r][c] == 'v':
                q.append((r, c, 1, 0))
            elif grid[r][c] == '<':
                q.append((r, c, 0, -1))
    
    count = 0
    while q:
        r, c, dr, dc = q.popleft()
        if grid[r][c] != 'X':
            count += 1
        grid[r][c] = 'X'
        nextR, nextC = r + dr, c + dc
        if nextR > -1 and nextR < m and nextC > -1 and nextC < n:
            if grid[nextR][nextC] == '#':
                newDR, newDC = dc, -dr
                nextR, nextC = r + newDR, c + newDC
                if nextR > -1 and nextR < m and nextC > -1 and nextC < n:
                    q.append((nextR, nextC, newDR, newDC))
            else:
                q.append((nextR, nextC, dr, dc))
    [print(row) for row in grid]
    return count


def part2(grid):
    pass


if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            row = []
            for letter in l:
                row.append(letter)
            grid.append(row)

        if sys.argv[2] == "part1":
            print(f'Part 1 Answer = {part1(grid)}')
        if sys.argv[2] == "part2":
            print(f'Part 2 Answer = {part2(grid)}')