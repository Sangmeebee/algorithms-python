n = int(input())
arr = []
for _ in range(n):
    word = input()
    word_count = len(word)
    arr.append((word_count, word))

arr = list(set(arr))
arr.sort(key=lambda x: (x[0], x[1]))
for v in arr:
    print(v[1])
