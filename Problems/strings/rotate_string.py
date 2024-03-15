# write a python program to rotate a string


def rotate_string(input_str, n):
    # Calculate the actual rotation position
    n = n % len(input_str)
    
    # Rotate the string
    rotated_str = input_str[n:] + input_str[:n]
    
    return rotated_str

# Test the function
input_str = "hello"
rotation_positions = 2
print("Original string:", input_str)
print("Rotated string:", rotate_string(input_str, rotation_positions))
