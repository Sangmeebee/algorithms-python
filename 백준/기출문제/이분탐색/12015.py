from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = []

for i in arr:
    k = bisect_left(dp, i)
    if k >= len(dp):
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))
