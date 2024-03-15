# Check if number is palindrom. String case is very easy use [::-1] or 
# write a simple function to reverse order of characters.

def is_palindrome(number):
    if number < 0:
        return False
    temp = number
    reversed = 0
    while temp > 0:
        rem = temp % 10
        reversed = reversed * 10 + rem
        temp = temp // 10
    # print(reversed)
    return 'Yes' if number == reversed else 'Not'

number = int(input("Enter number: "))
print(is_palindrome(number))