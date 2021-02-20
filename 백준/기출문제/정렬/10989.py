import sys
arr = [0] * 10001
for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    arr[num] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    for j in range(arr[i]):
        print(i)
