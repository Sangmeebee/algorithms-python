import heapq, sys

n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
h = []

for v in arr:
    if v != 0:
        heapq.heappush(h, (abs(v), v))
    else:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
