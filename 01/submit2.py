import sys
import collections

left = collections.Counter()
right = collections.Counter()
n = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        a, b = line.split("   ")
        left[int(a)] += 1
        right[int(b)] += 1

answer = 0
for k, v in left.items():
    answer += (k * right[k]) * v

print(answer)
