n=int(input("Enter a number "))
i=2
p=1
if(n<=1):
     p=0
if(n==2):
    p=1
while i<n:
    if(n%i==0):
        p=0
        break
    i+=1
if(p==1):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")