# 최단 경로
# 최소 힙을 이용한 다익스트라

import heapq

def dijkstra(start) :
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    for i in graph[now] :
      cost = dist + i[1]
      if distance[i[0]] > cost :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

n, m, c = map(int, input().split())
INF = 1001
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

dijkstra(c)

result = []
for i in range(1, len(distance)) :
  if distance[i] != INF and distance[i] != 0 :
    result.append(distance[i])

print(len(result), max(result))