numbers=[1,2,3,4,5]
print(numbers)
rttci=list(map(lambda base, index: base**index, numbers, range(len(numbers))))
print("Numbers after raising to their respective indexes")
print(rttci)