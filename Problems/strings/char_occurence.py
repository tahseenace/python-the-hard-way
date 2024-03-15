string = "aabcccccyyyyyyyyyyyy"

count = {}
for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
max_val = max(count.values())
print(f'max occurrence is {max_val}')
max_key = [key for key, value in count.items() if value == max_val]
print(f'key for max occurence is {max_key}')