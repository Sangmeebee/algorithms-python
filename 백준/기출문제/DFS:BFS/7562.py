from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        if (a, b) == end:
            break
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[a][b] + 1
                    q.append((nx, ny))


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    bfs(start[0], start[1])
    print(arr[end[0]][end[1]])
