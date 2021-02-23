n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [1] * n
arr.sort(key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])
print(n - max(dp))
