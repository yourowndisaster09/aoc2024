import sys
from collections import defaultdict


def part1(grid):
    m = len(grid)
    n = len(grid[0])

    def valid(r, c):
        return r >= 0 and r < m and c >= 0 and c < n

    antennas = defaultdict(list)
    for r in range(m):
        for c in range(n):
            antenna = grid[r][c]
            if antenna != '.':
                antennas[antenna].append((r, c))

    antinodes = set()
    for antenna, coors in antennas.items():
        numAntennas = len(coors)
        for i in range(numAntennas):
            for j in range(i + 1, numAntennas):
                a = coors[i]
                b = coors[j]
                dy = b[0] - a[0]
                dx = b[1] - a[1]

                r1, c1 = b[0] + dy, b[1] + dx
                if valid(r1, c1):
                    antinodes.add((r1, c1))

                r2, c2 = a[0] - dy, a[1] - dx
                if valid(r2, c2):
                    antinodes.add((r2, c2))
    return len(antinodes)



def part2(a):
    pass


if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            grid.append(l)

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(grid)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(grid)}')