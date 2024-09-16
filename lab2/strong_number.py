def fact(n):
    if (n == 0 or n == 1):
        return 1
    return (n * fact(n - 1))

x = int(input("Enter number to find whether it is a strong number or not: "))
sumon = 0
on = x

if (x < 0):
    print(x, "is not a strong number.")
elif (x == 0):
    print("0 is not a strong number.")
else:
    while x > 0:
        c = x % 10
        x = x // 10
        sumon += fact(c)
    if (sumon == on):
        print(on, "is a strong number.")
    else:
        print(on, "is not a strong number.")


    
  