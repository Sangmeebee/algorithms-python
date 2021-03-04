from collections import deque
n, k = map(int, input().split())
INF = int(1e9)
visited = [False] * 100001
dp = [0] * 100001

def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        if v == k:
            break
        if v - 1 >= 0 and not visited[v - 1]:
            visited[v - 1] = True
            dp[v - 1] = dp[v] + 1
            q.append(v - 1)
        if v + 1 <= 100000 and not visited[v + 1]:
            visited[v + 1] = True
            dp[v + 1] = dp[v] + 1
            q.append(v + 1)
        if v * 2 <= 100000 and not visited[v * 2]:
            visited[v * 2] = True
            dp[v * 2] = dp[v] + 1
            q.append(v * 2)

bfs(n)
print(dp[k])
