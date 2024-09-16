n1=float(input("Enter first number"))
n2=float(input("Enter second number"))
q=str(input("Enter operator + or - or * or /"))
if q == '+' :
    print(n1, q, n2 ,'=', n1+n2)
elif q == '-' :
    print(n1,q,n2,'=',n1-n2)
elif q =='*' :
    print(n1,q,n2,'=',n1*n2)
elif q == '/':
    print(n1,q,n2,'=',n1/n2)
else :
    print("Invalid operator")
    