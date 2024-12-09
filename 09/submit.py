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


def part2(data):
    moved = []
    i = 0
    free = False
    total = 0
    nums = {}
    available = {}
    for d in data:
        count = int(d)
        if free:
            available[total] = count
        else:
            nums[total] = count
        for _ in range(count):
            if free:
                moved.append(None)
            else:
                moved.append(i)
        total += count
        if not free:
            i += 1
        free = not free

    # print(nums)
    # print(available)
    # print(moved)

    for x in sorted(nums.keys(), reverse=True):
        match = None
        for y in sorted([k for k in available.keys() if k < x]):
            if available[y] >= nums[x]:
                match = y
                break

        if match is not None:
            # print(f"Move {nums[x]} at {x} to {y}")
            for i in range(nums[x]):
                moved[y + i] = moved[x + i]
                moved[x + i] = None
            # print(moved)
            remaining = available[y] - nums[x]
            if remaining:
                available[y + nums[x]] = remaining
            del available[y]
            # print(available)
    # print(moved)

    return sum([i * v for i, v in enumerate(moved) if v is not None])


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