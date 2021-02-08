# 동적 계획법 (Bottom up)
# n*m개의 위치에 금의 개수를 입력
# 윗행, 지금 행, 아래 행으로 금을 캘 수 있다고 할 때 최대로 캘 수 있는 금의 양은?

for _ in range(int(input())) :
  n, m = map(int, input().split())
  arr = list(map(int, input().split())) 

  dp = []
  for i in range(n) :
    dp.append(arr[(i*m):(i+1)*m])

  for j in range(1, m) :
    for i in range(n) :
      if i == 0 : left_up = 0
      else : left_up = dp[i-1][j-1]
      if i == n-1 : left_down = 0
      else : left_down = dp[i+1][j-1]
      left = dp[i][j-1]

      dp[i][j] += max(left_up, left, left_down)

  result = 0
  for i in range(n) :
    result = max(result, dp[i][m-1])
  print(result)