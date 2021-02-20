import sys
arr = []
for _ in range(int(input())):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
for v in arr:
    print(v)
