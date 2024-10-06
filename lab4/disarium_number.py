def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num
num=int(input("Enter your number "))
if is_disarium(num):
        print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")