n = int(input())
count = 0
for i in range(n):
    arr = list(str(i))
    s = i
    for j in arr:
        s += int(j)
    if s == n:
        break
    count += 1
if s == n:
    print(count)
else:
    print(0)
