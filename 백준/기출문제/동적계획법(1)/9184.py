MAX = 21

dp = [[[0] * MAX for _ in range(MAX)] for __ in range(MAX)]


def cal_w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return cal_w(20, 20, 20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = cal_w(a, b, c - 1) + cal_w(a, b - 1, c - 1) - cal_w(
            a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = cal_w(a - 1, b, c) + cal_w(a - 1, b - 1, c) + cal_w(
        a - 1, b, c - 1) - cal_w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {cal_w(a, b, c)}')
