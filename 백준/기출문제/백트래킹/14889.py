from itertools import combinations
n = int(input())
res = int(1e9)
num_list = [i for i in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def solve():
    global res

    for i in combinations(num_list, n // 2):
        start = list(i)
        link = list(set(num_list) - set(i))

        start_comb = list(combinations(start, 2))
        link_comb = list(combinations(link, 2))

        start_sum = 0
        for i, j in start_comb:
            start_sum += (arr[i][j] + arr[j][i])
        link_sum = 0
        for i, j in link_comb:
            link_sum += (arr[i][j] + arr[j][i])

        res = min(res, abs(start_sum - link_sum))


solve()
print(res)
