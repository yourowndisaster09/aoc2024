import sys
from math import *
from time import *
from collections import *
from heapq import *
from re import *

ARROWS = ['^', '>', 'v', '<', 'A']
ARROW_DIRS = {
    'A': [None, None, '>', '^'],
    '<': [None, 'v', None, None],
    '^': [None, 'A', 'v', None],
    '>': ['A', None, None, 'v'],
    'v': ['^', '>', None, '<'],
}
NUM_DIRS = {
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

def minCostToClickDir1(start, end):
    q = deque([(start, 0)])
    V = set()

    while q:
        cursor, count = q.popleft()
        if cursor == end:
            return count + 1
        if cursor in V:
            continue
        V.add(cursor)
        for dir in ARROW_DIRS[cursor]:
            if dir and dir not in V:
                q.append((dir, count + 1))

DIR1_COSTS = defaultdict(dict)
for a in ARROWS:
    for b in ARROWS:
        DIR1_COSTS[a][b] = minCostToClickDir1(a, b)
for u, costs in DIR1_COSTS.items():
    for v, w in costs.items():
        print(f'DIR1: {u} to {v} = {w}')

def minCostToClickDir2(start, end):
    D = {}
    V = {}
    for i in range(5):
        key = ARROWS[i]
        D[key] = inf
        V[key] = False
    arrowI = ARROWS.index(start)
    D[arrowI] = 0

    pq = [(0, start, 'A')]
    while pq:
        cost, cursor1, cursor2 = heappop(pq)
        if V[cursor1]:
            continue
        V[cursor1] = True
        for i, nextCursor1 in enumerate(ARROW_DIRS[cursor1]):
            if nextCursor1 and not V[nextCursor1]:
                nextCursor2 = ARROWS[i]
                nextCost = cost + DIR1_COSTS[cursor2][nextCursor2]
                # print(f"{cursor1} to {nextCursor1} = {cursor2} to {nextCursor2} = {DIR1_COSTS[cursor2][nextCursor2]}")
                if nextCursor1 == end:
                    # print(f"{cursor1} to {nextCursor1} = {nextCursor2} to A = {DIR1_COSTS[nextCursor2]['A']} (CLICK)")
                    nextCost += DIR1_COSTS[nextCursor2]['A']
                    nextCursor2 = 'A'
                D[nextCursor1] = min(D[nextCursor1], nextCost)
                heappush(pq, (D[nextCursor1], nextCursor1, nextCursor2))
    return D[end]

DIR2_COSTS = defaultdict(dict)
for a in ARROWS:
    for b in ARROWS:
        if a == b:
            DIR2_COSTS[a][b] = 1
        else:
            DIR2_COSTS[a][b] = minCostToClickDir2(a, b)
for u, costs in DIR2_COSTS.items():
    for v, w in costs.items():
        print(f'DIR2: {u} to {v} = {w}')

COST_TO_MOVE = {
    '^': 12,
    '<': 18,
    '>': 10,
    'v': 16
}

def numKeypad(start, end):
    D = {}
    V = {}
    for i in range(11):
        key = 'A' if i == 10 else str(i)
        D[key] = inf
        V[key] = False
    D[start] = 0

    pq = [(0, start, 'A')]
    while pq:
        cost, number, cursor = heappop(pq)
        if V[number]:
            continue
        V[number] = True
        for i, nextNumber in enumerate(NUM_DIRS[number]):
            if nextNumber and not V[nextNumber]:
                nextCursor = ARROWS[i]
                nextCost = cost + COST_TO_MOVE[nextCursor]
                print(f"{number} to {nextNumber} = {cursor} to {nextCursor} = {COST_TO_MOVE[nextCursor]}")
                if nextNumber == end:
                    print(f"{number} to {nextNumber} = {nextCursor} to A = 1 (CLICK)")
                    nextCost += 1
                    nextCursor = 'A'
                D[nextNumber] = min(D[nextNumber], nextCost)
                heappush(pq, (D[nextNumber], nextNumber, nextCursor))
    return D[end]


def part1(data):
    complexities = 0
    for code in data:
        start = 'A'
        cost = 0
        for end in code:
            cost += numKeypad(start, end)
            start = end
        print(cost)
        print()
        complexities += (cost * int(sub("[^0-9]", "", code)))

    return complexities


def part2(data):
    pass


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