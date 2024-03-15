string = "This bike is awesome"
list = string.split()
list2 = []
for word in list:
    word = word[::-1]
    list2.append(word)
formatted = " ".join(list2)
print(formatted)
