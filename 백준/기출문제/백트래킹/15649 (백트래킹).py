n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
def dfs(count) :
  if count == m :
    print(*arr)
    return
  for i in range(1, n+1) :
    if visited[i] :
      continue
    visited[i] = True
    arr.append(i)
    dfs(count+1)
    arr.pop()
    visited[i] = False

dfs(0)
