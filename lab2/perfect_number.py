x=int(input("Enter a number to find whether the number is a perfect number or not: "))
sum=1
for i in range(2,x):
    if (x%i==0):
        sum=sum+i
if sum==x:
    print(x, "is a perfect number.")
else:
    print(x, "is not a perfect number.")