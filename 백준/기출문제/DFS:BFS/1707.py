from collections import deque
t = int(input())

def bfs(start):
    global stop
    q = deque([start])
    color[start] = 1
    while q and not stop:
        x = q.popleft()
        c = 3 - color[x]
        for j in arr[x]:
            if color[j] == 0:
                color[j] = c
                q.append(j)
            elif color[j] == color[x]:
                stop = True
                break


for _ in range(t):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    stop = False
    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in range(1, v + 1):
        if stop:
            break
        if color[i] > 0:
            continue
        bfs(i)

    if not stop:
        print("YES")
    else:
        print("NO")
