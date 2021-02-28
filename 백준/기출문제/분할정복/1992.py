n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

def solve(x, y, size):
    check = arr[x][y]
    if size == 1:
        return check

    result = []
    for i in range(x, x + size):
        for j in range(y, y + size):
            if check != arr[i][j]:
                result.append('(')
                result.extend(solve(x, y, size // 2))
                result.extend(solve(x, y + size // 2, size // 2))
                result.extend(solve(x + size // 2, y, size // 2))
                result.extend(solve(x + size // 2, y + size // 2, size // 2))
                result.append(')')

                return result
    return check

print(''.join(solve(0, 0, n)))
