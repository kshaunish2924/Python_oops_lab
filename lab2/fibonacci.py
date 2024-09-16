def fibonacci(n):
    a=0
    b=1
    if (n>=1):
       print(a, end=" ")
    if(n>=2):
       print(b, end=" ")
    for i in range(3,n+1):
       nf=a+b
       print(nf, end=" ")
       a,b=b,nf
    
   
n=int(input("Enter number of terms "))
fibonacci(n)