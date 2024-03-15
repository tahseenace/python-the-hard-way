def countvowels(input_str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)

input_str = input("Enter String: ")
print(countvowels(input_str))