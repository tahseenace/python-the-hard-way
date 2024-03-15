# Write a Python program to get a string from a given string where all 
# occurrences of its first char have been changed to "@", except the first 
# char itself

sentence = 'mohammad tahseen'
ch = sentence[0]
sentence = sentence.replace(ch, '@')
print(sentence)
sentence = ch + sentence[1:]
print(sentence)

# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string

a = 'abc'
b = 'xyz'

print(f'Before swap: {a} {b}')
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print(f'After swap: {a1} {b1}')


