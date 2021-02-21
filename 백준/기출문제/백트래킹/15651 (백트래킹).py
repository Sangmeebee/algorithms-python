n, m = map(int, input().split())
num_list = [i for i in range(n+1)]
arr = []

def dfs(count, idx) :
  if count == m :
    print(*arr)
    return

  for i in range(idx, n+1) :
    arr.append(num_list[i])
    dfs(count+1, i)
    arr.pop()

dfs(0, 1)
