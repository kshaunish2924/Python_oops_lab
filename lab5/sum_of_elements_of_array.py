def sumOfElementsOfArray(array):
    aai=list(map(int,array))
    soa=sum(aai)
    return soa
array=input("Enter the elements separated by spaces: ").split()
result=sumOfElementsOfArray(array)
print("The sum of the elements of the array is: ",result)