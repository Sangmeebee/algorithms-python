n = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(1, n + 1):
        count += min(mid // i, n)
    if count >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
