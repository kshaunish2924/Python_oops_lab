x=int(input("Enter number whose factorial is to be found: "))
if x<0:
    print("Enter non negative number to find factorial ")
elif (x==0 or x==1):
    print("The factorial of ",x, "is 1.")
elif (x>1):
    product=1
    for i in range(2,x+1):
        product=product*i
    print("The factorial of ",x, "is", product,".")