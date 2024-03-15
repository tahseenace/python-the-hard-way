# Question: Write a function to perform basic string compression using the counts of repeated characters.
# Explanation: Given a string like "aaabbcccc", the function should return "a3b2c4". This tests the candidate's ability to manipulate strings and count character occurrences.

def compress_string(s):
    compressed = ""
    count = 1

    # Iterate through the string, starting from the second character
    for i in range(1, len(s)):
        # If the current character is the same as the previous one, increase the count
        if s[i] == s[i - 1]:
            count += 1
        else:
            # If the current character is different, append the previous character and its count
            compressed += s[i - 1] + str(count)
            count = 1  # Reset the count for the new character

    # Append the last character and its count
    compressed += s[-1] + str(count)

    # Return the compressed string only if it is shorter than the original string
    return compressed if len(compressed) < len(s) else s

# Test the function
print(compress_string("aaabbcccc"))  # Output: "a3b2c4"
