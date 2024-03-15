def common_prefix(strings):
    if not strings:
        return ""

    # Find the minimum length string in the list
    min_length = min(len(s) for s in strings)
    # print(f'short word: {min_length}')
    
    # Iterate through each character position
    for i in range(min_length):
        # Check if all characters at position i are the same
        if len(set(s[i] for s in strings)) > 1:
            return strings[0][:i]  # Return the common prefix
    # If we reach this point, all characters up to min_length are the same
    return strings[0][:min_length]


strings = ["flower", "flow", "flowight"]

# print("Common Prefix:", common_prefix(strings))
print(f'Common prefix: {common_prefix(strings)}')