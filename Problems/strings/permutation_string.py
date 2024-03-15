# Question: Write a function to generate all permutations of a given string.
# Explanation: This question tests the candidate's understanding of recursion and string manipulation.

def generate_permutations(input_str):
    # Base case: if the string is empty or has only one character, return it as a single permutation
    if len(input_str) <= 1:
        return [input_str]

    # Initialize an empty list to store permutations
    permutations = []

    # Iterate over each character in the input string
    for i in range(len(input_str)):
        # Extract the current character
        current_char = input_str[i]

        # Generate all permutations of the remaining characters by recursion
        remaining_chars = input_str[:i] + input_str[i + 1:]
        remaining_permutations = generate_permutations(remaining_chars)

        # Append the current character to each permutation of the remaining characters
        for perm in remaining_permutations:
            permutations.append(current_char + perm)

    return permutations

# Test the function
input_str = "abc"
print("Permutations of '{}' are:".format(input_str))
print(generate_permutations(input_str))
