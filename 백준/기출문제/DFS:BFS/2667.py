n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
count_arr = []
count = 0

def dfs(x, y):
    global count
    graph[x][y] = 0
    count += 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            count_arr.append(count)
            count = 0

print(len(count_arr))
count_arr.sort()
for v in count_arr:
    print(v)
