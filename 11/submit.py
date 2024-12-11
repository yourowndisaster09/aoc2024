import sys
from collections import defaultdict

def part1(stones):
    for i in range(25):
        nextStones = []
        for stone in stones:
            if stone == 0:
                nextStones.append(1)
            else:
                stoneStr = str(stone)
                lenStone = len(stoneStr)
                if lenStone % 2 == 0:
                    nextStones.append(int(stoneStr[:(lenStone // 2)]))
                    nextStones.append(int(stoneStr[(lenStone // 2):]))
                else:
                    nextStones.append(stone * 2024)
        stones = nextStones
    return len(stones)


def part2(stones):
    memo = defaultdict(int)
    def countWays(stone, n):
        if n == 0:
            return 1
        if (stone, n) in memo:
            return memo[(stone, n)]
        if stone == 0:
            memo[(stone, n)] = countWays(1, n - 1)
        else:
            stoneStr = str(stone)
            lenStone = len(stoneStr)
            if lenStone % 2 == 0:
                memo[(stone, n)] = countWays(int(stoneStr[:(lenStone // 2)]), n - 1) + countWays(int(stoneStr[(lenStone // 2):]), n - 1)
            else:
                memo[(stone, n)] = countWays(stone * 2024, n - 1)
        return memo[(stone, n)]
    answer = 0
    for stone in stones:
        answer += countWays(stone, 75)
    return answer


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        data = [int(x) for x in f.readline().strip().split(" ")]

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(data)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(data)}')