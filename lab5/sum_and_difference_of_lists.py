list1=[1,2,3,4,5]
list2=[5,4,3,2,1]
print("List1=",list1)
print("List2=",list2)
sol=list(map(lambda x,y: x+y, list1,list2))
dol=list(map(lambda x,y: x-y, list1,list2))
print("The sum of the lists is: ",sol)
print("The difference of the lists is: ",dol)