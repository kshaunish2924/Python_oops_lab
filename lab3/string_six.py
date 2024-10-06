string = "Hello, World!"
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print(f"The number of vowels in the string is: {count}")