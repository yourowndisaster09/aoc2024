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
    w = {}
    for a, op, b, z in wires:
        w[f'{a} {op} {b}'] = z

    def findWire(a, op, b):
        test1 = f'{a} {op} {b}'
        if test1 in w:
            return (w[test1], test1)
        test2 = f'{b} {op} {a}'
        if test2 in w:
            return (w[test2], test2)
        print("Missing wire", a, op, b)
        assert False

    swaps = []
    z = {}
    z[0] = 'z00'
    c = {}
    c[0], _ = findWire('x00', 'AND', 'y00')
    for i in range(1, 45):
        p1, _ = findWire(f'x{i:02}', 'XOR', f'y{i:02}')
        p2 = c[i - 1]
        try:
            posZ, posWire = findWire(p1, 'XOR', p2)
        except:
            corrZ = f'z{i:02}'
            print("No wire for", corrZ, p1, p2)
            realWire = [key for key, value in w.items() if value == corrZ][0]
            a, op, b = realWire.split(' ')
            if a == p2:
                rightP1 = b
            else:
                rightP1 = a
            realWire = [key for key, value in w.items() if value == rightP1][0]
            wrongWire = [key for key, value in w.items() if value == p1][0]
            w[wrongWire] = rightP1
            w[realWire] = p1
            swaps.append(rightP1)
            swaps.append(p1)
            print("SWAP", rightP1, p1)

        if posZ[0] == 'z':
            z[i] = posZ
        else:
            corrZ = f'z{i:02}'
            realWire = [key for key, value in w.items() if value == corrZ][0]
            w[posWire] = corrZ
            w[realWire] = posZ
            z[i] = corrZ
            swaps.append(corrZ)
            swaps.append(posZ)
            print("SWAP", corrZ, posZ)

        c1, _ = findWire(f'x{i:02}', 'AND', f'y{i:02}')
        c2a, _ = findWire(f'x{i:02}', 'XOR', f'y{i:02}')
        c2b = c[i - 1]
        c2, _ = findWire(c2a, 'AND', c2b)
        c[i], _ = findWire(c1, 'OR', c2)

    return ",".join(sorted(swaps))


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