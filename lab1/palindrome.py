n=int(input("Enter a number "))
rev=0
on=n
while n>0:
    rev=(rev*10)+(n%10)
    n=n//10
if(rev==on):
    print(on,"is a palindrome.")
else:
    print(on,"is not a palindrome.")