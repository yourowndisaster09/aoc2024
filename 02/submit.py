import sys

countSafe = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        a = [int(x) for x in line.split(" ")]
        n = len(a)
        if n == 1:
            countSafe += 1
        else:
            inc = a[1] > a[0]
            safe = True
            for i in range(1, n):
                diff = a[i] - a[i - 1]
                if inc:
                    if diff < 1 or diff > 3:
                        safe = False
                        break
                else:
                    if diff > -1 or diff < -3:
                        safe = False
                        break
            if safe:
                countSafe += 1

print(countSafe)
