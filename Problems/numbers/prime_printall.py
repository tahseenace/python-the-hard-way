number = int(input("Enter number: "))

def is_prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3:
        return True
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

for x in range(number):
    if is_prime(x) is True:
        print(x)