import sys
from math import inf
from heapq import *

def part1(map, start, end):
    print(start, end)
    m = len(map)
    n = len(map[0])

    VECTOR = {
        0: (-1, 0), # UP
        1: (0, 1),  # RIGHT
        2: (1, 0),  # DOWN
        3: (0, -1)  # LEFT
    }

    V = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
    D = [[[inf for _ in range(4)] for _ in range(n)] for _ in range(m)]
    D[start[0]][start[1]][1] = 0
    pq = [(0, start, 1)]

    while pq:
        score, pos, o = heappop(pq)
        r, c = pos

        if V[r][c][o]:
            continue
        V[r][c][o] = True

        nextSteps = [
            (r, c, (o + 1) % 4, 1000),
            (r, c, (o + 2) % 4, 1000),
            (r, c, (o + 3) % 4, 1000),
            (r + VECTOR[o][0], c + VECTOR[o][1], o, 1),
        ]

        for nR, nC, nO, addedScore in nextSteps:
            print(nR, nC, nO)
            if nR > -1 and nR < m and nC > -1 and nC < n and not V[nR][nC][nO] and map[nR][nC] != '#':
                D[nR][nC][nO] = min(
                    D[nR][nC][nO],
                    score + addedScore
                )
                heappush(pq, (D[nR][nC][nO], (nR, nC), nO))
    return min(D[end[0]][end[1]])


def part2(map, start, end):
    print(start, end)
    m = len(map)
    n = len(map[0])

    VECTOR = {
        0: (-1, 0), # UP
        1: (0, 1),  # RIGHT
        2: (1, 0),  # DOWN
        3: (0, -1)  # LEFT
    }

    V = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
    D = [[[inf for _ in range(4)] for _ in range(n)] for _ in range(m)]
    C = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
    D[start[0]][start[1]][1] = 0
    pq = [(0, start, 1)]

    while pq:
        score, pos, o = heappop(pq)
        r, c = pos

        if V[r][c][o]:
            continue
        V[r][c][o] = True

        nextSteps = [
            (r, c, (o + 1) % 4, 1000),
            (r, c, (o + 2) % 4, 1000),
            (r, c, (o + 3) % 4, 1000),
            (r + VECTOR[o][0], c + VECTOR[o][1], o, 1),
        ]

        for nR, nC, nO, addedScore in nextSteps:
            print(nR, nC, nO)
            if nR > -1 and nR < m and nC > -1 and nC < n and not V[nR][nC][nO] and map[nR][nC] != '#':
                D[nR][nC][nO] = min(
                    D[nR][nC][nO],
                    score + addedScore
                )
                heappush(pq, (D[nR][nC][nO], (nR, nC), nO))
    return min(D[end[0]][end[1]])


if __name__ == "__main__":
    data = []
    start = None
    end = None
    with open(sys.argv[1], 'r') as f:
        i = 0
        for line in f:
            l = line.strip()
            if not l:
                break
            if 'S' in l:
                start = (i, l.index('S'))
            if 'E' in l:
                end = (i, l.index('E'))
            data.append(l)
            i += 1

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, start, end)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data, start, end)}')