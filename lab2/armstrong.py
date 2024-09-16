n=int(input("Enter number to find whether its an Armstrong number or not: "))
on=n
count=0
sum=0
while n>0:
    n=n//10
    count=count+1
n=on
while n>0:
    c=n%10
    n=n//10
    sum=sum+(c**count)
if sum==on:
    print(on, "is an Armstrong number.")
else:
    print(on, " is not an Armstrong number.")
