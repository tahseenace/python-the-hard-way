def most_freq_char(input_string):
    count = {}
    for char in input_string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    max_count = max(value for key, value in count.items())
    max_key = [key for key, value in count.items() if value == max_count]
    return [max_key, max_count]
    # return max(value for key,value in count.items())

input_string = input("Enter string: ")
print(most_freq_char(input_string))