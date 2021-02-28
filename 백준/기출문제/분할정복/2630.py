import sys
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

w_count = 0
b_count = 0

def cut(x, y, n):
    global w_count, b_count
    color = dp[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if dp[i][j] != color:
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        w_count += 1
        return
    else:
        b_count += 1
        return

cut(0, 0, n)
print(w_count)
print(b_count)
