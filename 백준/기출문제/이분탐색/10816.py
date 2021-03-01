from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr_search = list(map(int, input().split()))

for v in arr_search:
    left_search = bisect_left(arr, v)
    right_search = bisect_right(arr, v)
    print(right_search - left_search, end=' ')
