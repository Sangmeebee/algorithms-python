n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr_search = list(map(int, input().split()))


def binary_search(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(target, start, mid-1)
    else:
        return binary_search(target, mid+1, end)


for v in arr_search:
    print(binary_search(v, 0, n - 1))
