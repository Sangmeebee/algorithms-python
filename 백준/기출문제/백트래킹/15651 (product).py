from itertools import product
n, m = map(int, input().split())
num_list = [i for i in range(1, n + 1)]
result = list(product(num_list, repeat=m))

for i in result:
    for j in i:
        print(j, end=' ')
    print()
