import sys
from collections import deque, defaultdict
from bisect import insort

def part1(garden):
    m = len(garden)
    n = len(garden[0])

    price = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if not visited[r][c]:
                q = deque([(r, c)])
                count = 0
                perimeter = 0
                while q:
                    i, j = q.popleft()
                    if visited[i][j]:
                        continue
                    visited[i][j] = True
                    count += 1
                    nextPlants = [
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1),
                    ]
                    for nI, nJ in nextPlants:
                        if nI > -1 and nI < m and nJ > -1 and nJ < n and garden[nI][nJ] == garden[i][j]:
                            if not visited[nI][nJ]:
                                q.append((nI, nJ))
                        else:
                            perimeter += 1
                price += (count * perimeter)
    return price



def part2(garden):
    m = len(garden)
    n = len(garden[0])

    price = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if not visited[r][c]:
                q = deque([(r, c)])
                count = 0
                f = defaultdict(set)
                while q:
                    i, j = q.popleft()
                    if visited[i][j]:
                        continue
                    visited[i][j] = True
                    count += 1
                    nextPlants = [
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1),
                    ]
                    for nI, nJ in nextPlants:
                        if nI > -1 and nI < m and nJ > -1 and nJ < n and garden[nI][nJ] == garden[i][j]:
                            if not visited[nI][nJ]:
                                q.append((nI, nJ))
                        else:
                            if nI == i:
                                if nJ > j:
                                    f[(nJ, 2)].add(i)
                                else:
                                    f[(nJ, 0)].add(i)
                            if nJ == j:
                                if nI > i:
                                    f[(nI, 1)].add(j)
                                else:
                                    f[(nI, 3)].add(j)
                fences = 0
                for k, vals in f.items():
                    valsSort = sorted(vals)
                    prev = valsSort[0] - 1
                    c = 1
                    for val in valsSort:
                        if prev != val - 1:
                            c += 1
                        prev = val
                    fences += c

                price += (count * (fences))
    return price


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            data.append(l)

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')