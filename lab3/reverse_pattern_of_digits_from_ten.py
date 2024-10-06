num = 1
for i in range(1, 5):
    start = num + i - 1
    end = num - 1
    for j in range(start, end, -1):
        print(f'{j} ', end='')
    num = start + 1
    print()