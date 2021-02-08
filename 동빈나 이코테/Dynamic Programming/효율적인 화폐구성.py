# 동적 계획법 (Bottom up)
# n, m 에 화폐 개수, 총 금액 이 주어진다
# 한 줄마다 n의 값을 지정한다

n, m = map(int, input().split())
ln = []
for _ in range(n) :
  ln.append(int(input()))

d = [10001]*(m+1)
d[0] = 0

for i in range(n) :
  for j in range(ln[i], m+1) :
    if d[j - ln[i]] != 10001 :
      d[j] = min(d[j], d[j-ln[i]]+1)

if d[m] == 10001 :
  print(-1)
else :
  print(d[m])
