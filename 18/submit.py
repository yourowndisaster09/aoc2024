import sys
from math import inf


def part1(bytes, m, firstBytes):
    space = [['.' for _ in range(m)] for _ in range(m)]
    print(bytes, m, firstBytes)
    for i in range(firstBytes):
        x, y = bytes[i]
        space[y][x] = '#'
    [print(''.join(s)) for s in space]

    D = [[inf for _ in range(m)] for _ in range(m)]
    D[0][0] = 0
    V = [[False for _ in range(m)] for _ in range(m)]
    pq = [(0, (0, 0))]

    while pq:
        d, (r, c) = pq.pop(0)
        if V[r][c]:
            continue
        V[r][c] = True
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < m:
                if space[nr][nc] == '.' and not V[nr][nc]:
                    D[nr][nc] = min(D[nr][nc], d + 1)
                    pq.append((D[nr][nc], (nr, nc)))
    
    return D[m-1][m-1]


def part2(a):
    pass


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            data.append([int(b) for b in l.split(',')])
    size = int(sys.argv[3]) + 1
    firstBytes = int(sys.argv[4])

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, size, firstBytes)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')