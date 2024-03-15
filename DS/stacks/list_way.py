
# push >> append (adds elements to the end)
# pop  >> pop (removes element from the end)

stack = []
print(len(stack))
stack.append(10)
stack.append(20)
stack.append('tahseen')
print(len(stack))
stack.append(30)
stack.append(40)
print(stack)
print(len(stack))
stack.pop()
print(stack)
stack.pop()
print(stack)
print(len(stack))

# last/top element
print(stack[-1])


# Better implementation usng functions
stack2 = []

def push():
    element = input("Enter the element: ")
    stack2.append(element)
    print(element)

def pop_element():
    if not stack2:
        print("Stack is empty!")
    else:
        e = stack2.pop()
        print(f"Removed element: {e}")
        print(stack2)

while True:
    print("Select the operation 1. Push 2. Pop 3. Quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation!")