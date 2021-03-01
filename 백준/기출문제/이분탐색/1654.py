import sys
k, n = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]

end = max(arr)
result = []

def binary_search(start, end):
    if start > end:
        return
    count = 0
    mid = (start + end) // 2
    for v in arr:
        count += v // mid
    if count >= n:
        result.append(mid)
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)

binary_search(1, end)
print(max(result))
