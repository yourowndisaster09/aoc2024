import sys
import re
import time


def part1(robots, m, n, time):
    midX = n // 2
    midY = m // 2

    q1 = q2 = q3 = q4 = 0
    for p, v in robots:
        locX = (p[0] + (v[0] * time)) % n
        locY = (p[1] + (v[1] * time)) % m
        print(locY, locX)
        if locX < midX and locY < midY:
            q1 += 1
        elif locX > midX and locY < midY:
            q2 += 1
        elif locX < midX and locY > midY:
            q3 += 1
        elif locX > midX and locY > midY:
            q4 += 1
    return q1 * q2 * q3 * q4


def part2(robots, m, n):
    numRobots = len(robots)
    robotPositions = [r[0] for r in robots]
    t = 0
    while True:
        graph = [['.' for _ in range(n)] for _ in range(m)]
        t += 1
        for i in range(numRobots):
            locX = (robotPositions[i][0] + robots[i][1][0]) % n
            locY = (robotPositions[i][1] + robots[i][1][1]) % m
            graph[locY][locX] = '+'
            robotPositions[i] = (locX, locY)
        if ''.join(graph[0]) == '..................................................+..................................................':
            print(t)
            [print(''.join(g)) for g in graph]
            print()


if __name__ == "__main__":
    data = []
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            match = re.findall(pattern, l)[0]
            data.append(((int(match[0]), int(match[1])), (int(match[2]), int(match[3]))))

    if sys.argv[2] == "test1":
        print(f'Test Answer = {part1(data, 7, 11, 100)}')
    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, 103, 101, 100)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data, 103, 101)}')