n = int(input())
a = list(map(int, input().split()))
dp_increase = [1] * n
dp_decrease = [0] * n
max_num = 1
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp_increase[i] = max(dp_increase[j] + 1, dp_increase[i])
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)
for i in range(n):
    max_num = max(max_num, dp_increase[i] + dp_decrease[i])
print(max_num)
