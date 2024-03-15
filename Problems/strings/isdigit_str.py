# Calculate the sum and average of the digits present in a string

# What to remember: isdigit()
# Usage: char.isdigit()
# int(char)

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)
