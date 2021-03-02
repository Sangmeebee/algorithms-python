import sys
sys.setrecursionlimit(50000)

t = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def dfs(x, y, m, n):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny, m, n)


for _ in range(t):
    m, n, k = map(int, input().split())
    res = 0
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                res+=1
                dfs(i, j, m, n)
    print(res)
