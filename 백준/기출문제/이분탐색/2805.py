from bisect import bisect_right
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
start, end = 0, arr[-1]
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(bisect_right(arr, mid), n):
        count += (arr[i] - mid)
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
