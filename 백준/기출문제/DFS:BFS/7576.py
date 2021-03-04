from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()
is_true = False
result = -1
for i in graph:
    for j in i:
        if j == 0:
            is_true = True
        result = max(result, j)

if is_true:
    print(-1)
else:
    if result == -1:
        print(0)
    else:
        print(result - 1)
