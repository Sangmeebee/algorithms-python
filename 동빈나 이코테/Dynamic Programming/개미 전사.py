# 동적 계획법(Top Down)
n = int(input())
k = list(map(int, input().split()))

d = [0]*n

def top_down(x) :
  if x < 2 :
    d[x] = k[x] 
  if d[x] != 0 :
    return d[x]
  d[x] = max(top_down(x-2) + k[x], top_down(x-1))
  return d[x]
print(top_down(n-1))


# 동적 계획법(Bottom Up)
n = int(input())
k = list(map(int, input().split()))

d = [0]*n
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n) :
  d[i] = max(d[i-2] + k[i], d[i-1])
print(d[n-1])