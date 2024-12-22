import sys
from math import *
from time import *
from collections import *
from heapq import *
from re import *
from functools import cache

DIRS = ['^', '>', 'v', '<', 'A']
DIRPAD = {
    '^': [None, 'A', 'v', None],
    '>': ['A', None, None, 'v'],
    'v': ['^', '>', None, '<'],
    '<': [None, 'v', None, None],
    'A': [None, None, '>', '^'],
}
DIR_PATHS = {
    'A': {
        '^': ['<A'],
        '>': ['vA'],
        'v': ['<vA', 'v<A'],
        '<': ['v<<A', '<v<A'],
        'A': ['A'],
    },
    '^': {
        '^': ['A'],
        '>': ['>vA', 'v>A'],
        'v': ['vA'],
        '<': ['v<A'],
        'A': ['>A'],
    },
    '>': {
        '^': ['^<A', '<^A'],
        '>': ['A'],
        'v': ['<A'],
        '<': ['<<A'],
        'A': ['^A'],
    },
    'v': {
        '^': ['^A'],
        '>': ['>A'],
        'v': ['A'],
        '<': ['<A'],
        'A': ['^>A', '>^A']
    },
    '<': {
        '^': ['>^A'],
        '>': ['>>A'],
        'v': ['>A'],
        '<': ['A'],
        'A': ['>>^A', '>^>A']
    }
}

@cache
def bestPath(a, b, depth):
    if depth == 1:
        return len(DIR_PATHS[a][b][0])
    minPath = inf
    for path in DIR_PATHS[a][b]:
        lenPath = 0
        start = 'A'
        for end in path:
            lenPath += bestPath(start, end, depth - 1)
            start = end
        minPath = min(minPath, lenPath)
    return minPath

COSTS = defaultdict(dict)
for a in DIRS:
    for b in DIRS:
        COSTS[a][b] = bestPath(a, b, 25)

NUMPAD = {
    'A': ['3', None, None, '0'],
    '0': ['2', 'A', None, None],
    '1': ['4', '2', None, None],
    '2': ['5', '3', '0', '1'],
    '3': ['6', None, 'A', '2'],
    '4': ['7', '5', '1', None],
    '5': ['8', '6', '2', '4'],
    '6': ['9', None, '3', '5'],
    '7': [None, '8', '4', None],
    '8': [None, '9', '5', '7'],
    '9': [None, None, '6', '8'],
}

def clickNumPad(start, end):
    D = defaultdict(dict)
    V = defaultdict(dict)
    for i in range(11):
        key = 'A' if i == 10 else str(i)
        for dir in DIRS:
            D[key][dir] = inf
            V[key][dir] = False
    D[start]['A'] = 0

    pq = [(0, start, 'A')]
    while pq:
        # print(f"{pq}")
        cost, number, cursor = heappop(pq)
        if V[number][cursor]:
            continue
        V[number][cursor] = True
        for i, nextNumber in enumerate(NUMPAD[number]):
            nextCursor = DIRS[i]
            if nextNumber and not V[nextNumber][nextCursor]:
                nextCost = cost + COSTS[cursor][nextCursor]
                # print(f"{number} to {nextNumber} = {cursor} to {nextCursor} = {COSTS[cursor][nextCursor]}")
                if nextNumber == end:
                    # print(f"{number} to {nextNumber} = {nextCursor} to A = 1 (CLICK)")
                    nextCost += COSTS[nextCursor]['A']
                    nextCursor = 'A'
                if nextCost < D[nextNumber][nextCursor]:
                    D[nextNumber][nextCursor] = nextCost
                    # print(f"Push {(D[nextNumber][nextCursor], nextNumber, nextCursor)}")
                    heappush(pq, (D[nextNumber][nextCursor], nextNumber, nextCursor))
    return min(D[end].values())

def part1(data):
    complexities = 0
    for code in data:
        start = 'A'
        cost = 0
        for end in code:
            cost += clickNumPad(start, end)
            start = end
        print(cost)
        complexities += (cost * int(sub("[^0-9]", "", code)))
    return complexities


def part2(data):
    complexities = 0
    for code in data:
        start = 'A'
        cost = 0
        for end in code:
            cost += clickNumPad(start, end)
            start = end
        complexities += (cost * int(sub("[^0-9]", "", code)))
    return complexities


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            data.append(line)

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')