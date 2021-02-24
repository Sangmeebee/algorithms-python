n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

count = 0
for i in arr:
    if k >= i:
        temp = k % i
        count += k // i
        k = temp

    if k == 0:
        break
print(count)
