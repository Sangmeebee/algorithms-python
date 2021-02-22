dp = [0] * 101
dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2

t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))

def cal(x):
    for i in range(5, x + 1):
        dp[i] = dp[i - 1] + dp[i - 5]

i = max(arr)
cal(i)
for j in arr:
    print(dp[j])
