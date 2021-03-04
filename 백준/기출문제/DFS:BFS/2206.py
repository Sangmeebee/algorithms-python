from collections import deque
n, m = map(int, input().split())
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
graph = [list(map(int, input())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == -1:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
                elif z == 0 and graph[nx][ny] == 1 and visited[nx][ny][
                        z + 1] == -1:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    q.append((nx, ny, z + 1))


bfs()
ans1, ans2 = visited[n - 1][m - 1][0], visited[n - 1][m - 1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))
