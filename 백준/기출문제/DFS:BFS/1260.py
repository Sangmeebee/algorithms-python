from collections import deque
n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


def dfs(start):
    dfs_visited[start] = True
    print(start, end=' ')
    for i in range(1, n+1) :
        if not dfs_visited[i] and arr[start][i] :
            dfs(i)


def bfs(start):
    q = deque([start])
    bfs_visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(1, n+1) :
            if not bfs_visited[i] and arr[now][i] :
                q.append(i)
                bfs_visited[i] = True

dfs(v)
print()
bfs(v)
