x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
if (x<y):
    (x,y)=(y,x)
lcm=x*y+1
for i in range(x,(x*y+1)):
    if (i%x==0 and i%y==0):
        lcm=i
        break
print("the lcm of ",x,"and",y,"is",lcm)
gcd=y
for i in range(y,1,-1):
    if(y%i==0 and x%i==0):
        gcd=i
        break
print("The gcd of",x,"and",y,"is",gcd)