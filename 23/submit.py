import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(data):
    adj = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        adj[a].add(b)
        adj[b].add(a)

    comps = set()
    for k, connections in adj.items():
        n = len(connections)
        listCon = list(connections)
        for i in range(n):
            for j in range(i + 1, n):
                if listCon[j] in adj[listCon[i]]:
                    comps.add(tuple(sorted([k, listCon[i], listCon[j]])))
    # print(len(comps))
    count = 0
    for c in comps:
        hasT = False
        for t in c:
            if t[0] == 't':
                hasT = True
                break
        if hasT:
            count += 1
    return count


def part2(data):
    adj = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        adj[a].add(b)
        adj[b].add(a)
    maxLen = 0
    validList = None
    for k, connections in adj.items():
        n = len(connections)
        listCon = list(connections)
        for i in range(n):
            valid = set([k])
            valid.add(listCon[i])
            for j in range(i + 1, n):
                add = True
                for v in valid:
                    if listCon[j] not in adj[v]:
                        add = False
                        break
                if add:
                    valid.add(listCon[j])
            if len(valid) > maxLen:
                validList = valid
                maxLen = len(valid)
    return ','.join(sorted(validList))


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