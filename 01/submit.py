import sys
import heapq

pq1 = []
pq2 = []
n = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        a, b = line.split("   ")
        heapq.heappush(pq1, int(a))
        heapq.heappush(pq2, int(b))
        n += 1
answer = 0
for i in range(n):
    m = heapq.heappop(pq1)
    n = heapq.heappop(pq2)
    answer += abs(m - n)

print(answer)
