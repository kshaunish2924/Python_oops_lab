def nCr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
result = nCr(n, r)
print(f"{n}C{r} is {result}")