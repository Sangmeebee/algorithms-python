import sys 

n = sys.stdin.readline().rstrip()
arr = list(map(int, n))

arr.sort(reverse=True)
arr = map(str, arr)
print(''.join(arr))
