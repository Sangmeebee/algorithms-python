#시뮬레이션 유형, 구현 유형, 완전 탐색 유형

S = list(input())
summ = 0
lstr = []
for v in S :
  if v.isdigit() :
    summ += int(v)
  else :
    lstr.append(v)
res = ''.join(sorted(lstr))
if summ != 0 :
  res+=str(summ)
print(res)
