import sys

# Topological Sort - DFS method
def topologicalSort(adj):
    visited = set()
    TS = []

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        for x in adj[n]:
            dfs(x)
        TS.append(n)

    for x in adj.keys():
        if x not in visited:
            dfs(x)

    return list(reversed(TS))


def part1(rules, updates):
    answer = 0
    for update in updates:
        n = len(update)
        adj = {}
        for x, y in rules:
            if x not in update or y not in update:
                continue
            if x not in adj:
                adj[x] = []
            if y not in adj:
                adj[y] = []
            adj[x].append(y)
        TS = topologicalSort(adj)

        # Just my assumption for this problem - all pages have rules; otherwise we have multiple possible TS
        if len(TS) != len(update):
            assert False

        if TS == update:
            # print(update, int(update[n // 2]))
            answer += int(update[n // 2])
        
    return answer


def part2(rules, updates):
    answer = 0
    for update in updates:
        n = len(update)
        adj = {}
        for x, y in rules:
            if x not in update or y not in update:
                continue
            if x not in adj:
                adj[x] = []
            if y not in adj:
                adj[y] = []
            adj[x].append(y)
        TS = topologicalSort(adj)

        # Just my assumption for this problem - all pages have rules; otherwise we have multiple possible TS
        if len(TS) != len(update):
            assert False

        if TS != update:
            # print(update, TS)
            answer += int(TS[n // 2])
        
    return answer


if __name__ == "__main__":
    rules = []
    updates = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if not line.strip():
                break
            rules.append(line.strip().split("|"))
        for line in f:
            if line.strip():
                updates.append(line.strip().split(","))
        # print(all(([len(x) % 2 == 1 for x in updates])))
        if sys.argv[2] == "part1":
            print(f'Part 1 Answer = {part1(rules, updates)}')
        if sys.argv[2] == "part2":
            print(f'Part 2 Answer = {part2(rules, updates)}')