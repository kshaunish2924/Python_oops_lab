x=int(input("Enter the number"))
n=int(input("Enter the power"))

def power(x, n):
    pow = 1
    for i in range(n):
        pow = pow * x

    return pow
print(power(x,n))