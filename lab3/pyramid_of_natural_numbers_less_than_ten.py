num = 1
for i in range(1, 10):
    for j in range(2 * i - 1):
        if num < 10:
            print(f'{num} ', end='')
            num += 1
    if num >= 10:
        break
    print()