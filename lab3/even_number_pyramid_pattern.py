n = 5
num = 10
for i in range(1, n + 1):
    for j in range(i):
        print(num - 2 * j, end=' ')
    print()