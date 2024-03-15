
def are_anagrams(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    count = {}
    # count of characters in str1
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # decrease the count of charaters in str2
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            return False # character is not there
        
    # compare the values
    for value in count.values():
        if value != 0:
            return False

    return True

str1 = "silent"
str2 = "listen"

print(are_anagrams(str1, str2))

###############################################################

# alternat direct program
# def are_anagrams(str1, str2):
# return sorted(str1) == sorted(str2)