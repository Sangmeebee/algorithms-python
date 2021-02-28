n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

minus_count = 0
zero_count = 0
plus_count = 0


def solve(x, y, size):
    global minus_count, zero_count, plus_count
    check = arr[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if check != arr[i][j]:
                for k in range(3):
                    for l in range(3):
                        solve(x + k * size // 3, y + l * size // 3, size // 3)
                return
    if check == -1:
        minus_count += 1
    elif check == 0:
        zero_count += 1
    else:
        plus_count += 1
    return


solve(0, 0, n)
print(minus_count)
print(zero_count)
print(plus_count)
