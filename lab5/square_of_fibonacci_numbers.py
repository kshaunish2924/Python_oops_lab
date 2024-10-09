def fibonacci(n):
    fib_seq=[]
    a=0
    b=1
    for _ in range(n):
        fib_seq.append(a)
        a,b=b,a+b
    return fib_seq
def square(x):
    x=x**2
    return x
N=int(input("Enter the value of N: "))
fibnumbers=fibonacci(N)
squaredfibnumbers=list(map(square,fibnumbers))
print(squaredfibnumbers)
    