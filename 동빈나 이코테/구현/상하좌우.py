#시뮬레이션 유형, 구현 유형, 완전 탐색 유형 

import sys
n = int(input())
li = list(sys.stdin.readline().rstrip().split())

x, y = 1, 1

#    동  서  남  북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

move_type = {'R' : 0, 'L' : 1, 'D' : 2, 'U' : 3}

for i in li :
  nx = x + dx[move_type[i]]
  ny = y + dy[move_type[i]]

  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue
  x, y = nx, ny
print(x, y)
