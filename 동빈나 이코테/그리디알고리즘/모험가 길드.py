import sys
n = int(input())
li = list(map(int, sys.stdin.readline().rstrip().split()))
li = sorted(li)

temp = []
count = 0

for i in li :
  temp.append(i)
  if len(temp) >= i :
    temp = []
    count+=1
print(count)
