n = int(input())
data = list(map(int, input().split()))
sum_list = [data[0]]
for i in range(n - 1):
    sum_list.append(max(sum_list[i] + data[i + 1], data[i + 1]))
print(max(sum_list))
