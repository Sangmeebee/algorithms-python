n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(v):
    global count
    visited[v] = True
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count - 1)
