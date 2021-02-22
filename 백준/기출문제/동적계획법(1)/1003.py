test_case = [0] * 41
test_case[1] = 1
arr = []
for i in range(int(input())):
    arr.append(int(input()))


def fibo(x):
    if x == 0:
        return 0
    if test_case[x] != 0:
        return test_case[x]
    test_case[x] = fibo(x - 1) + fibo(x - 2)
    return test_case[x]


for x in arr:
    if x == 0:
        print(1, 0)
    else:
        fibo(x)
        print(test_case[x - 1], test_case[x])
