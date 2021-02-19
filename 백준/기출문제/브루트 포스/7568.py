n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

rank_arr = []
for i in range(len(arr)):
    rank = 1
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                rank += 1
    rank_arr.append(rank)

for rank in rank_arr:
    print(rank, end=' ')
