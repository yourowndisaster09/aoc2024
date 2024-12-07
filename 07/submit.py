import sys


def part1(equations):
    def backtrack(answer, nums, i, n, total):
        if i == n:
            return total == answer
        if total > answer:
            return False
        return backtrack(answer, nums, i + 1, n, total + nums[i]) or backtrack(answer, nums, i + 1, n, total * nums[i])

    sumTrue = 0
    for equation in equations:
        answer, nums = equation
        if backtrack(answer, nums, 1, len(nums), nums[0]):
            sumTrue += answer
    return sumTrue

def part2(equations):
    def backtrack(answer, nums, i, n, total):
        if i == n:
            return total == answer
        if total > answer:
            return False
        return (
            backtrack(answer, nums, i + 1, n, total + nums[i]) or 
            backtrack(answer, nums, i + 1, n, total * nums[i]) or 
            backtrack(answer, nums, i + 1, n, int(str(total) + str(nums[i])))
        )

    sumTrue = 0
    for equation in equations:
        answer, nums = equation
        if backtrack(answer, nums, 1, len(nums), nums[0]):
            sumTrue += answer
    return sumTrue

if __name__ == "__main__":
    equations = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip()
            if not l:
                break
            answer, nums = l.split(": ")
            answer = int(answer)
            nums = list(map(int, nums.split(" ")))
            equations.append((answer, nums))
    
    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(equations)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(equations)}')