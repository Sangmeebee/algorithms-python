# ㅇㅣㅈㅣㄴㅌㅏㅁㅅㅐㄱ

from bisect import bisect_right
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

start = 0
end = li[-1]

while True :
  mid = (start+end)//2
  sumV = 0
  for i in range(bisect_right(li, mid), n) :
    sumV+= (li[i]-mid)
  if sumV > m :
    start = mid+1
  elif sumV < m :
    end = mid-1
  else :
    print(mid)
    break
  
