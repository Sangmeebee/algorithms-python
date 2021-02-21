n, m = map(int, input().split())
arr = []
def dfs(count, idx) :
  if count == m :
    print(*arr)
    return
  for i in range(idx, n+1) :
    arr.append(i)
    dfs(count+1, i)
    arr.pop()

dfs(0, 1)
