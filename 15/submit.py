import sys
from collections import deque
from time import sleep

def part1(loc, map, moves):
    m = len(map)
    n = len(map[0])
    # [print(g) for g in map]
    # print()
    # sleep(1)

    for move in moves:
        r, c = loc
        if move == '<':
            nC = c - 1
            while nC > 0 and map[r][nC] == 'O':
                nC -= 1
            if map[r][nC] == '#':
                continue
            for j in range(nC, c - 1):
                map[r][j] = 'O'
            map[r][c - 1] = '@'
            map[r][c] = '.'
            loc = (r, c - 1)

        elif move == '>':
            nC = c + 1
            while nC < n - 1 and map[r][nC] == 'O':
                nC += 1
            if map[r][nC] == '#':
                continue
            for j in range(c + 2, nC + 1):
                map[r][j] = 'O'
            map[r][c + 1] = '@'
            map[r][c] = '.'
            loc = (r, c + 1)

        elif move == '^':
            nR = r - 1
            while nR > 0 and map[nR][c] == 'O':
                nR -= 1
            if map[nR][c] == '#':
                continue
            for i in range(nR, r - 1):
                map[i][c] = 'O'
            map[r - 1][c] = '@'
            map[r][c] = '.'
            loc = (r - 1, c)

        elif move == 'v':
            nR = r + 1
            while nR < m - 1 and map[nR][c] == 'O':
                nR += 1
            if map[nR][c] == '#':
                continue
            for i in range(r + 2, nR + 1):
                map[i][c] = 'O'
            map[r + 1][c] = '@'
            map[r][c] = '.'
            loc = (r + 1, c)

        # print(f"Move = {move}")
        # [print(g) for g in map]
        # print()
        # sleep(1)

    # [print(g) for g in map]
    # print()
    ans = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if map[r][c] == 'O':
                # print(r, c)
                ans += (100 * r + c)
    return ans


def part2(loc, map, moves):
    m = len(map)
    n = len(map[0])
    # [print(''.join(g)) for g in map]
    # print()

    for move in moves:
        r, c = loc
        if move == '<':
            nC = c - 1
            while nC > 0 and map[r][nC] == ']':
                nC -= 2
            if map[r][nC] == '#':
                continue
            for j in range(nC, c - 1, 2):
                map[r][j] = '['
                map[r][j + 1] = ']'
            map[r][c - 1] = '@'
            map[r][c] = '.'
            loc = (r, c - 1)

        elif move == '>':
            nC = c + 1
            while nC < n - 1 and map[r][nC] == '[':
                nC += 2
            if map[r][nC] == '#':
                continue
            for j in range(c + 2, nC + 1, 2):
                map[r][j] = '['
                map[r][j + 1] = ']'
            map[r][c + 1] = '@'
            map[r][c] = '.'
            loc = (r, c + 1)

        elif move == '^':
            nR = r - 1
            c1 = c2 = c
            nextRow = map[nR][c1:c2 + 1]
            q = deque()
            while nR > 0 and '#' not in nextRow and (']' in nextRow or '[' in nextRow):
                if nextRow[0] == ']':
                    c1 -= 1
                else:
                    x = 0
                    while nextRow[x] == '.':
                        x += 1
                    c1 += x
                if nextRow[-1] == '[':
                    c2 += 1
                else:
                    x = len(nextRow) - 1
                    while nextRow[x] == '.':
                        x -= 1
                        c2 -= 1
                nR -= 1
                q.append((c1, c2))
                nextRow = map[nR][c1:c2 + 1]
            if '#' in nextRow:
                continue
            for i in range(nR, r - 1):
                c1, c2 = q.pop()
                for j in range(c1, c2 + 1):
                    map[i][j] = map[i + 1][j]
                    map[i + 1][j] = '.'
            map[r - 1][c] = '@'
            map[r][c] = '.'
            loc = (r - 1, c)

        elif move == 'v':
            nR = r + 1
            c1 = c2 = c
            nextRow = map[nR][c1:c2 + 1]
            q = deque()
            while nR < m - 1 and '#' not in nextRow and (']' in nextRow or '[' in nextRow):
                if nextRow[0] == ']':
                    c1 -= 1
                else:
                    x = 0
                    while nextRow[x] == '.':
                        x += 1
                    c1 += x
                if nextRow[-1] == '[':
                    c2 += 1
                else:
                    x = len(nextRow) - 1
                    while nextRow[x] == '.':
                        x -= 1
                        c2 -= 1
                nR += 1
                q.append((c1, c2))
                nextRow = map[nR][c1:c2 + 1]
            if '#' in nextRow:
                continue
            for i in range(nR, r + 1, -1):
                c1, c2 = q.pop()
                for j in range(c1, c2 + 1):
                    map[i][j] = map[i - 1][j]
                    map[i - 1][j] = '.'
            map[r + 1][c] = '@'
            map[r][c] = '.'
            loc = (r + 1, c)

        # print(f"Move = {move}")
        # [print(''.join(g)) for g in map]
        # print()
        # sleep(0.05)

    # [print(g) for g in map]
    # print()
    ans = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if map[r][c] == '[':
                # print(r, c)
                ans += (100 * r + c)
    return ans


if __name__ == "__main__":
    if sys.argv[2] == "part1":
        map = []
        robotLocation = None
        moves = ''
        with open(sys.argv[1], 'r') as f:
            i = 0
            for line in f:
                l = line.strip()
                if not l:
                    break
                if '@' in l:
                    robotLocation = (i, l.index('@'))
                map.append(list(l))
                i += 1

            for line in f:
                l = line.strip()
                if not l:
                    break
                moves += l
        print(f'Part 1 Answer = {part1(robotLocation, map, moves)}')

    if sys.argv[2] == "part2":

        map = []
        robotLocation = None
        moves = ''
        with open(sys.argv[1], 'r') as f:
            i = 0
            for line in f:
                l = line.strip()
                if not l:
                    break
                mapRow = []
                for c in l:
                    if c == '.':
                        mapRow.append(c)
                        mapRow.append(c)
                    elif c == 'O':
                        mapRow.append('[')
                        mapRow.append(']')
                    elif c == '@':
                        mapRow.append(c)
                        mapRow.append('.')
                    elif c == '#':
                        mapRow.append(c)
                        mapRow.append(c)
                if '@' in mapRow:
                    robotLocation = (i, mapRow.index('@'))
                map.append(mapRow)
                i += 1

            for line in f:
                l = line.strip()
                if not l:
                    break
                moves += l
        print(f'Part 2 Answer = {part2(robotLocation, map, moves)}')