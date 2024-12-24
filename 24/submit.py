import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(data, wires):
    print(data, wires)

    w = deque(wires)
    while w:
        x, op, y, z = w.popleft()
        if x in data and y in data:
            if op == 'AND':
                data[z] = data[x] & data[y]
            elif op == 'OR':
                data[z] = data[x] | data[y]
            elif op == 'XOR':
                data[z] = data[x] ^ data[y]
        else:
            w.append((x, op, y, z))
    keys = sorted([k for k in data.keys() if k[0] == 'z'])
    binNum = ''
    for k in keys:
        binNum = str(data[k]) + binNum
    return int(binNum, 2)


def part2(data, wires):
    n = len(wires)
    keys = data.keys()
    xs = sorted([k for k in keys if k[0] == 'x'], reverse=True)
    ys = sorted([k for k in keys if k[0] == 'y'], reverse=True)
    x = int(''.join([str(data[x]) for x in xs]), 2)
    y = int(''.join([str(data[y]) for y in ys]), 2)
    zBin = list(bin(x + y)[2:])
    required = {}
    i = 0
    while zBin:
        key = f'z{i:02}'
        required[key] = int(zBin.pop())
        i += 1
    print(required)


    # Model as dag
    adj = defaultdict(list)
    outdegrees = defaultdict(int)
    oppositeAdj = defaultdict(list)
    for a, op, b, z in wires:
        key = f'{a} {op} {b}'
        adj[a].append(key)
        adj[b].append(key)
        adj[key].append(z)

        outdegrees[a] += 1
        outdegrees[b] += 1
        outdegrees[key] += 1

        oppositeAdj[z].append(key)
        oppositeAdj[key].append(a)
        oppositeAdj[key].append(b)

        if z[0] == 'z':
            if op != 'XOR' and z[1:] != '45':
                print(key, z)
        else:
            if a[0] not in {'x', 'y'} and b[0] not in {'x', 'y'}:
                if op == 'XOR':
                    print(key, z)

    def traverse(k, tab=0):
        print(f"{''.join(['  '] * tab)}{k} = {oppositeAdj[k]}")
        for neighbor in oppositeAdj[k]:
            for n in oppositeAdj[neighbor]:
                traverse(n, tab + 1)
    traverse('z03')



    w = deque(wires)
    while w:
        x, op, y, z = w.popleft()
        if x in data and y in data:
            if op == 'AND':
                data[z] = data[x] & data[y]
            elif op == 'OR':
                data[z] = data[x] | data[y]
            elif op == 'XOR':
                data[z] = data[x] ^ data[y]
        else:
            w.append((x, op, y, z))
    current = {k: v for k, v in data.items() if k[0] == 'z'}

    # print(data)
    # for k in required.keys():
    #     if current[k] != required[k]:
    #         print(f"Wrong {k}, needs {required[k]} but got {current[k]}")
    #         if input("Continue? ") == 'n':
    #             break

    #         # visited = set()
    #         # q = deque([k])
    #         # while q:
    #         #     node = q.popleft()
    #         #     if node in visited:
    #         #         continue
    #         #     print("  ", node)
    #         #     visited.add(node)
    #         #     for neighbor in oppositeAdj[node]:
    #         #         if neighbor not in visited:
    #         #             q.append(neighbor)


    # # print({k for k, v in outdegrees.items() if v == 0})






if __name__ == "__main__":
    data = {}
    wires = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            a, b = line.split(': ')
            data[a] = int(b)
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            a, c = line.split(' -> ')
            a, op, b = a.split(' ')
            wires.append((a, op, b, c))

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, wires)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data, wires)}')