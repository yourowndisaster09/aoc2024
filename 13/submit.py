import sys
from math import inf, isclose


def part1(machines):
    totalCost = 0
    for a, b, p in machines:
        minCost = inf
        for i in range(100):
            for j in range(100):
                if i * a[0] + j * b[0] == p[0] and i * a[1] + j * b[1] == p[1]:
                    minCost = min((3 * i) + j, minCost)
        if minCost is not inf:
            totalCost += minCost
    return totalCost


def part2(machines):
    totalCost = 0
    for a, b, p in machines:
        p = [10000000000000 + num for num in p]

        x = round(((p[0] - (p[1] * b[0] / b[1]))) / ((a[0] - (a[1] * b[0] / b[1]))))
        y = round((p[1] - (x * a[1])) / b[1])
        
        c1 = x * a[0] + y * b[0]
        if not c1 == p[0]:
            continue
        c2 = x * a[1] + y * b[1]
        if not c2 == p[1]:
            continue
        
        totalCost += 3 * x + y
    return totalCost


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        line = f.readline()
        while line:
            buttonA = [int(b.split('+')[1]) for b in line.strip().split(": ")[1].split(', ')]
            buttonB = [int(b.split('+')[1]) for b in f.readline().strip().split(": ")[1].split(', ')]
            price = [int(b.split('=')[1]) for b in f.readline().strip().split(": ")[1].split(', ')]
            data.append([buttonA, buttonB, price])
            f.readline()
            line = f.readline()

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')