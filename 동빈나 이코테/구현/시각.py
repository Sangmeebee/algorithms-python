#완전 탐색 유형

n = int(input())
count = 0
h = list(map(str, range(0, n+1)))
m = list(map(str, range(0, 60)))
s = list(map(str, range(0, 60)))
for i in h :
  for j in m :
    for k in s :
      if '3' in i+j+k :
        count+=1
print(count)
