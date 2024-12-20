import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(raceMap, start, end):
    print(raceMap, start, end)
    m = len(raceMap)
    n = len(raceMap[0])

    # BFS
    time = [[None for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = deque([(0, start)])
    while q:
        t, (r, c) = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        time[r][c] = t
        if (r, c) == end:
            break
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nR = r + dr
            nC = c + dc
            if 0 <= nR < m and 0 <= nC < n and not visited[nR][nC] and raceMap[nR][nC] != "#":
                q.append((t + 1, (nR, nC)))
    
    saves = defaultdict(list)
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = deque([(0, start)])
    while q:
        t, (r, c) = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        time[r][c] = t
        if (r, c) == end:
            break
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nR = r + dr
            nC = c + dc
            if 0 <= nR < m and 0 <= nC < n and not visited[nR][nC]:
                if raceMap[nR][nC] != "#":
                    q.append((t + 1, (nR, nC)))
                else:
                    maxSaveTime = -inf
                    for ddr, ddc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nnR = nR + ddr
                        nnC = nC + ddc
                        if 0 <= nnR < m and 0 <= nnC < n and not visited[nnR][nnC] and raceMap[nnR][nnC] != "#":
                            maxSaveTime = max(maxSaveTime, time[nnR][nnC] - t - 2)
                    if maxSaveTime > 0:
                        saves[maxSaveTime].append((nR, nC))
    [print(x) for x in time]
    count = 0
    for k, v in saves.items():
        print(k, len(v))
        if k >= 100:
            count += len(v)
    return count


def part2(raceMap, start, end, cap):
    m = len(raceMap)
    n = len(raceMap[0])

    # BFS
    time = [[None for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    visitedOrder = []
    q = deque([(0, start)])
    while q:
        t, (r, c) = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        visitedOrder.append((r, c))
        time[r][c] = t
        if (r, c) == end:
            break
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nR = r + dr
            nC = c + dc
            if 0 <= nR < m and 0 <= nC < n and not visited[nR][nC] and raceMap[nR][nC] != "#":
                q.append((t + 1, (nR, nC)))
    
    print(visitedOrder)
    lenVisitedOrder = len(visitedOrder)
    saves = defaultdict(int)
    for i in range(lenVisitedOrder):
        for j in range(i + 1, lenVisitedOrder):
            s = visitedOrder[i]
            e = visitedOrder[j]
            newTime = abs(s[0] - e[0]) + abs(s[1] - e[1])
            if newTime <= 20:
                oldTime = time[e[0]][e[1]] - time[s[0]][s[1]]
                savedTime = oldTime - newTime
                # print(f'{s} -> {e} savedTime = {savedTime}')
                saves[savedTime] += 1 
    count = 0
    for k, v in saves.items():
        print(k, v)
        if k >= cap:
            count += v
    return count


if __name__ == "__main__":
    data = []
    r = 0
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            if "S" in line:
                start = (r, line.index("S"))
            if "E" in line:
                end = (r, line.index("E"))
            data.append(line)
            r += 1

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, start, end)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data, start, end, int(sys.argv[3]))}')