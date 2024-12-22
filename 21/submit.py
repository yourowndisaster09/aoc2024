import sys
from math import *
from time import *
from collections import *
from heapq import *
from re import *

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

def bestPath(a, b):
    paths = []
    for path in DIR_PATHS[a][b]:
        prefix = ['']
        start = 'A'
        for end in path:
            newPrefix = []
            # print(f"{start} to {end} = {prefix} + {DIR_PATHS[start][end]}")
            for p in DIR_PATHS[start][end]:
                for pref in prefix:
                    newPrefix.append(pref + p)
            start = end
            prefix = newPrefix
        paths += prefix
    return min(paths, key=len)

COSTS = defaultdict(dict)
for a in DIRS:
    for b in DIRS:
        COSTS[a][b] = bestPath(a, b)

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

def clickNumPad(start, end, COST_TABLE):
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
                nextCost = cost + len(COST_TABLE[cursor][nextCursor])
                # print(f"{number} to {nextNumber} = {cursor} to {nextCursor} = {len(COST_TABLE[cursor][nextCursor])}")
                if nextNumber == end:
                    # print(f"{number} to {nextNumber} = {nextCursor} to A = 1 (CLICK)")
                    nextCost += len(COST_TABLE[nextCursor]['A'])
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
            cost += clickNumPad(start, end, COSTS)
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
            cost += clickNumPad(start, end, COSTS)
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