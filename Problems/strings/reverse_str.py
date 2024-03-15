string = "flower"

def reverse_string(string):
    reversed = ""
    for s in string:
        reversed = s + reversed
    return reversed

print(reverse_string(string))
print(string[::-1])
