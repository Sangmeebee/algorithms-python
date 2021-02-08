# 이진탐색

from bisect import bisect_left, bisect_right

def count_by_range(arr, x) :
  c = bisect_right(arr, x) - bisect_left(arr, x)
  if c > 0 :
    return c
  else :
    return None

n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(count_by_range(arr, x))
