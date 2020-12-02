ops = list(input())
res = int(ops[0])
for i in range(1, len(ops)) :
  op = int(ops[i])
  if op <=2 or res <=2 :
    res += op
  else :
    res *= op
print(res)