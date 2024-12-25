import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(data):
    keys = []
    locks = []
    for keylock in data:
        m = len(keylock)
        n = len(keylock[0])

        if all(k == '#' for k in keylock[0]) and all(k == '.' for k in keylock[m - 1]):
            lockHeights = []
            for j in range(n):
                height = 0
                for i in range(1, m - 1):
                    if keylock[i][j] == '#':
                        height += 1
                lockHeights.append(height)
            locks.append((lockHeights, m, n))
        else:
            keyHeights = []
            for j in range(n):
                height = 0
                for i in range(1, m - 1):
                    if keylock[i][j] == '#':
                        height += 1
                keyHeights.append(height)
            keys.append((keyHeights, m, n))

    count = 0
    for l, mL, nL in locks:
        for k, mK, nK in keys:
            if mL == mK and nL == nK and all([k[j] + l[j] <= mL - 2 for j in range(nL)]):
                count += 1
    return count


def part2(data):
    pass


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        lines = []
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                data.append(lines)
                lines = []
            else:
                lines.append(line)
        if lines:
            data.append(lines)

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')