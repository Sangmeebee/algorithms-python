import sys, heapq
n = int(input())
left, right = [], []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(left, (-right_value, right_value))
        heapq.heappush(right, (left_value, left_value))

    print(left[0][1])
