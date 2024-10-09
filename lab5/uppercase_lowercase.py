sequence="Manipal University Jaipur"
def upper_lower(seq):
    unique_characters=set(seq)
    lower=list(map(str.lower, unique_characters))
    upper=list(map(str.upper, unique_characters))
    return lower, upper
lower,upper=upper_lower(sequence)
print(sequence)
print("After manipulation:")
print(lower,upper)