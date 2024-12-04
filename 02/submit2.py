import sys

countSafe = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        a = [int(x) for x in line.split(" ")]
        n = len(a)
        if n == 1:
            countSafe += 1
        else:
            diffs = []
            for i in range(1, n):
                diffs.append(a[i] - a[i - 1])

            if all([d >= 1 and d <= 3 for d in diffs]):
                countSafe += 1
            elif all([d <= -1 and d >= -3 for d in diffs]):
                countSafe += 1
            else:
                for i in range(n):
                    if i == 0:
                        diffsPrime = diffs[1:]
                    elif i == n - 1:
                        diffsPrime = diffs[:n - 2]
                    else:
                        diffsPrime = diffs[:i] + diffs[i + 1:]
                        diffsPrime[i - 1] += diffs[i]
                    if all([d >= 1 and d <= 3 for d in diffsPrime]):
                        print("Mod", a, i,  diffsPrime)
                        countSafe += 1
                        break
                    if all([d <= -1 and d >= -3 for d in diffsPrime]):
                        print("Mod", a, i,  diffsPrime)
                        countSafe += 1
                        break

print(countSafe)
