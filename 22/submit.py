import sys
from math import *
from time import *
from collections import *
from heapq import *


def mix(secret, result):
    return result ^ secret

def part1(data, n):
    sumNthSecret = 0
    for secret in data:
        for i in range(n):
            result = secret * 64
            secret = result ^ secret
            secret = secret % 16777216
            result = secret // 32
            secret = result ^ secret
            secret = secret % 16777216
            result = secret * 2048
            secret = result ^ secret
            secret = secret % 16777216
        sumNthSecret += secret
    return sumNthSecret



def part2(data):
    sequences = defaultdict(dict)
    for i, secret in enumerate(data):
        prefix = []
        prev = secret % 10
        for _ in range(2000):
            result = secret * 64
            secret = result ^ secret
            secret = secret % 16777216
            result = secret // 32
            secret = result ^ secret
            secret = secret % 16777216
            result = secret * 2048
            secret = result ^ secret
            secret = secret % 16777216

            price = secret % 10
            prefix.append(price - prev)
            if len(prefix) > 3:
                key = tuple(prefix[-4:])
                if i not in sequences[key]:
                    sequences[key][i] = price
            prev = price
    maxBananas = -inf
    # print(sequences)
    for key, perBuyer in sequences.items():
        maxBananas = max(maxBananas, sum(perBuyer.values()))
    return maxBananas

if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                break
            data.append(int(line))

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data, 2000)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')