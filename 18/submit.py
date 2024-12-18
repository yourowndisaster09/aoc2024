import sys
from math import inf, isinf


def part1(bytes, m, firstBytes):
    space = [['.' for _ in range(m)] for _ in range(m)]
    print(bytes, m, firstBytes)
    for i in range(firstBytes):
        x, y = bytes[i]
        space[y][x] = '#'
    [print(''.join(s)) for s in space]

    V = [[False for _ in range(m)] for _ in range(m)]
    q = [(0, (0, 0))]

    while q:
        steps, (r, c) = q.pop(0)
        if V[r][c]:
            continue
        V[r][c] = True
        if r == m - 1 and c == m - 1:
            return steps
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < m:
                if space[nr][nc] == '.' and not V[nr][nc]:
                    q.append((steps + 1, (nr, nc)))


def part2(bytes, m):
    space = [['.' for _ in range(m)] for _ in range(m)]
    for i in range(len(bytes)):
        x, y = bytes[i]
        space[y][x] = '#'

        V = [[False for _ in range(m)] for _ in range(m)]
        q = [(0, (0, 0))]

        ends = False
        while q:
            steps, (r, c) = q.pop(0)
            if V[r][c]:
                continue
            V[r][c] = True
            if r == m - 1 and c == m - 1:
                ends = True
                break
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < m:
                    if space[nr][nc] == '.' and not V[nr][nc]:
                        q.append((steps + 1, (nr, nc)))
        
        if not ends:
            return ','.join([str(b) for b in bytes[i]])


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            data.append([int(b) for b in l.split(',')])
    size = int(sys.argv[3]) + 1

    if sys.argv[2] == "part1":
        firstBytes = int(sys.argv[4])
        print(f'Part 1 Answer = {part1(data, size, firstBytes)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data, size)}')