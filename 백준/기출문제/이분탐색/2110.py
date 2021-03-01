import sys
n, c = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    now = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= now + mid:
            count += 1
            now = arr[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)