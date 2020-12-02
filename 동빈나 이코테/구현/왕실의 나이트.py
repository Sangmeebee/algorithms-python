#시뮬레이션 유형, 구현 유형, 완전 탐색 유형

x, y = list(input())
count = 0
mv_x = [-2, -2, -1, 1, 2, 2, 1, -1]
mv_y = [-1, 1, 2, 2, 1, -1, -2, -2]

for i in range(len(mv_x)) :
  nx = ord(x)+mv_x[i]
  ny = int(y)+mv_y[i]

  if chr(nx) < 'a' or chr(nx) > 'h' or ny < 1 or ny >8 :
    continue
  else :
    count+=1
print(count)
