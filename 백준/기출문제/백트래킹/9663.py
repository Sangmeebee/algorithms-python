n = int(input())
arr = [0]*n
count = 0

def isTrue(x) :
  for i in range(x) :
    if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x-i :
      return False
  return True

def dfs(x) :
  global count

  if x == n :
    count+=1
  else :
    for i in range(n) :
      arr[x] = i
      if isTrue(x) :
        dfs(x+1)

dfs(0)
print(count)