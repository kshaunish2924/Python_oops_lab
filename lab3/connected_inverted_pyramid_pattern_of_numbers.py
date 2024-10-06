n = 5
for i in range(n):
    for j in range(n, i, -1):
        print(j, end=' ')
    for j in range(i):
        print(i + 1, end=' ')
    for j in range(i + 1, n + 1):
        print(j, end=' ')
    print()