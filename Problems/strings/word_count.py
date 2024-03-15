def count_word_occurrences(input_string):
 words = input_string.split()
 word_count = {}
 for word in words:
     if word in word_count:
        word_count[word] += 1
     else:
        word_count[word] = 1
 return word_count

input_string = "This Python program takes an input string, splits it into words, and then counts the occurrences of each word. Here's a breakdown of how it works"
print(count_word_occurrences(input_string))