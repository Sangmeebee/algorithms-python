from collections import deque
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dz = [-1, 1]

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[z][nx][ny] == 0:
                    graph[z][nx][ny] = graph[z][x][y] + 1
                    q.append((z, nx, ny))
        for i in range(2):
            nz = z + dz[i]
            if 0 <= nz < h and graph[nz][x][y] == 0:
                graph[nz][x][y] = graph[z][x][y] + 1
                q.append((nz, x, y))


for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k, i, j))

bfs()
is_true = False
result = -1
for g in graph:
    for i in g:
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
