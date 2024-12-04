import sys
from collections import deque

def part1(grid):
    m = len(grid)
    n = len(grid[0])

    def _getValidM(r, c):
        valid = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if r + dr > -1 and r + dr < m and c + dc > -1 and c + dc < n:
                    if grid[r + dr][c + dc] == "M":
                        valid.append(((r + dr, c + dc), (dr, dc), "M"))
        return valid

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "X":
                q = deque(_getValidM(r, c))
                while q:
                    coor, direction, letter = q.popleft()
                    if letter == "S":
                        count += 1
                        continue
                    i, j = coor
                    di, dj = direction
                    if i + di > -1 and i + di < m and j + dj > -1 and j + dj < n:
                        if letter == "M":
                            nextLetter = "A"
                        elif letter == "A":
                            nextLetter = "S"
                        if grid[i + di][j + dj] == nextLetter:
                            q.append(((i + di, j + dj), direction, nextLetter))
    return count


def part2(grid):
    m = len(grid)
    n = len(grid[0])
    count = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if grid[r][c] == "A":
                topLeft = grid[r - 1][c - 1]
                topRight = grid[r - 1][c + 1]
                bottomLeft = grid[r + 1][c - 1]
                bottomRight = grid[r + 1][c + 1]
                if topLeft == "M" and topRight == "M" and bottomRight == "S" and bottomLeft == "S":
                    count += 1
                elif topRight == "M" and bottomRight == "M" and bottomLeft == "S" and topLeft == "S":
                    count += 1
                elif bottomRight == "M" and bottomLeft == "M" and topLeft == "S" and topRight == "S":
                    count += 1
                elif bottomLeft == "M" and topLeft == "M" and topRight == "S" and bottomRight == "S":
                    count += 1
    return count


if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            grid.append(line.strip())
    
    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(grid)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(grid)}')