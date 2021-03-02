from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[a][b]+1
                q.append((nx, ny))

bfs(0, 0)
print(graph[n - 1][m - 1])
