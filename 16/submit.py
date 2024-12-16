import sys
from math import inf
from heapq import *
from collections import deque

def part1(map, start, end):
    # print(start, end)
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
            # print(nR, nC, nO)
            if nR > -1 and nR < m and nC > -1 and nC < n and not V[nR][nC][nO] and map[nR][nC] != '#':
                D[nR][nC][nO] = min(
                    D[nR][nC][nO],
                    score + addedScore
                )
                heappush(pq, (D[nR][nC][nO], (nR, nC), nO))
    return min(D[end[0]][end[1]])


def part2(map, start, end):
    m = len(map)
    n = len(map[0])

    VECTOR = {
        0: (-1, 0), # UP
        1: (0, 1),  # RIGHT
        2: (1, 0),  # DOWN
        3: (0, -1)  # LEFT
    }

    V = [[False for _ in range(4) for _ in range(n)] for _ in range(m)]
    D = [[inf for _ in range(4) for _ in range(n)] for _ in range(m)]
    D[start[0]][start[1]] = 0
    pq = [(0, start, 1)]

    while pq:
        score, pos, o = heappop(pq)
        r, c = pos

        if V[r][c]:
            continue
        V[r][c] = True

        for nO, val in VECTOR.items():
            dR, dC = val
            nR = r + dR
            nC = c + dC
            if nR > -1 and nR < m and nC > -1 and nC < n and not V[nR][nC] and map[nR][nC] != '#':
                addedScore = 1
                if o != nO:
                    addedScore += 1000
                D[nR][nC] = min(
                    D[nR][nC],
                    score + addedScore
                )
                heappush(pq, (D[nR][nC], (nR, nC), nO))
    # print(D[end[0]][end[1]])

    # BFS back to S
    V = [[False for _ in range(n)] for _ in range(m)]
    q = deque([(end, None)])
    while q:
        pos, prev = q.popleft()
        r, c = pos
        if V[r][c]:
            continue
        V[r][c] = True
        if pos == start:
            continue

        realScore = {}
        for o in range(4):
            reverseO = (o + 2) % 4
            nR = r + VECTOR[reverseO][0]
            nC = c + VECTOR[reverseO][1]
            if nR > -1 and nR < m and nC > -1 and nC < n and not V[nR][nC]:
                realScore[o] = D[nR][nC]
                if prev is not None and prev != o:
                    realScore[o] += 1000
        realMin = min(realScore.values())
        for o, score in realScore.items():
            if score == realMin:
                reverseO = (o + 2) % 4
                nR = r + VECTOR[reverseO][0]
                nC = c + VECTOR[reverseO][1]
                q.append(((nR, nC), o))

    count = 0
    for row in V:
        for val in row:
            if val:
                count += 1
    #[print([1 if x else 0 for x in v]) for v in V]
    return count


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