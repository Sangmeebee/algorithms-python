import sys
from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

print(int(round(sum(arr) / n, 0)))
print(arr[n // 2])

if n == 1:
    print(arr[0])
else:
    modes = Counter(arr).most_common()
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])

print(arr[-1] - arr[0])
