n = int(input())
prefix_sum = [0]
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    prefix_sum.append(prefix_sum[i] + arr[i])

print(sum(prefix_sum))
