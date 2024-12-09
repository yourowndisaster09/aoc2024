import sys
from collections import deque


def part1(data):
    q = deque()
    i = 0
    free = False
    for d in data:
        for _ in range(int(d)):
            if free:
                q.append(None)
            else:
                q.append(i)
        if not free:
            i += 1
        free = not free

    moved = []
    while q:
        item = q.popleft()
        if item is None:
            while q and q[-1] is None:
                q.pop()
            if q:
                item = q.pop()
        if item is not None:
            moved.append(item)
    return sum([i * v for i, v in enumerate(moved)])


def part2(a):
    pass


if __name__ == "__main__":
    data = None
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
        data = l

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')