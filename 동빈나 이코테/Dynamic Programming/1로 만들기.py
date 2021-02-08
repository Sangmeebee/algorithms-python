# 동적 계획법 (Bottom up)
# x를 5, 3, 2로 나누거나 1로 뺏을 때 1로 만들 수 있는 최소 연산 횟수  

x = int(input())
count = 0
d = [0]*30001

for i in range(2, x+1) :
  d[i] = d[i-1] + 1
  if i % 2 == 0 :
    d[i] = min(d[i], d[i//2] + 1)
  if i % 3 == 0 :
    d[i] = min(d[i], d[i//3] + 1)
  if i % 5 == 0 :
    d[i] = min(d[i], d[i//5] + 1)

print(d[x])
