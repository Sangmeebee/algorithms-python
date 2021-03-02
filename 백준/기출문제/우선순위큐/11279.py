import heapq, sys
n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
heap = []
for v in arr:
    if v > 0:
        heapq.heappush(heap, -v)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
