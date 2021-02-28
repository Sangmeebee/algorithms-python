n = int(input())
data = [0]*(n+1)
def fibonachi(n) :
  if n <= 1 :
    return n
  if data[n] != 0 :
    return data[n]
  data[n] = fibonachi(n-1) + fibonachi(n-2)
  return data[n]

print(fibonachi(n))