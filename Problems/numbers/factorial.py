# factorial of a number

number = int(input("Enter number: "))

# using regular loop
def factorial(number):
    initfact = 1
    for i in range(1,number+1):
        initfact = initfact * i
    return initfact

print(factorial(number))

# usin recursion
def factorial2(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)
    
print(factorial2(5))