import sys
from math import *
from time import *
from collections import *
from heapq import *


def part1(patterns, designs):
    count = 0
    for design in designs:
        n = len(design)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for j in range(1, n + 1):
            for i in range(j):
                if dp[i] and design[i:j] in patterns:
                    dp[j] = True
                    break
        if dp[n]:
            count += 1
    return count


def part2(patterns, designs):
    count = 0
    for design in designs:
        n = len(design)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for j in range(1, n + 1):
            for i in range(j):
                if design[i:j] in patterns:
                    dp[j] += dp[i]
        count += dp[n]
    return count


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        patterns = set(f.readline().strip().split(', '))
        f.readline()
        designs = []
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            designs.append(line.strip())

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(patterns, designs)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(patterns, designs)}')