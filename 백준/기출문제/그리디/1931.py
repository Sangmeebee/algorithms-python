n = int(input())
arr = []
count = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))
end = 0
count = 0
for i, j in arr:
    if i >= end:
        count += 1
        end = j
print(count)
