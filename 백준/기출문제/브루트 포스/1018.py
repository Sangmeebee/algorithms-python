n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

result_count = []

for i in range(n - 7):
    for j in range(m - 7):
        first_w = 0
        first_b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if arr[k][l] == 'W':
                        first_b += 1
                    else:
                        first_w += 1
                else:
                    if arr[k][l] == 'W':
                        first_w += 1
                    else:
                        first_b += 1
        result_count.append(first_w)
        result_count.append(first_b)

print(min(result_count))
