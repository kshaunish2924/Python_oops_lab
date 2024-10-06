n=int(input("Enter number "))
sum=0
for i in range(1,n-1):
    rem=n%10
    sum=sum+rem
    n=n//10
    
print(f"Sum of digits is {sum}")    
    