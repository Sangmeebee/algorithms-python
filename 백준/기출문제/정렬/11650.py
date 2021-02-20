n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key = lambda x : (x[0], x[1]))

for i in arr:
    print(i[0], i[1])
