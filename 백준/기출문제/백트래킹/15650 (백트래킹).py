n, m = map(int, input().split())
arr = []
visited = [False]*(n+1)
def dfs(count, idx) :
  if count == m :
    print(*arr)
    return
  for i in range(idx, n+1) :
    if visited[i] :
      continue
    visited[i] = True
    arr.append(i)
    dfs(count+1, i)
    arr.pop()
    visited[i] = False

dfs(0, 1)