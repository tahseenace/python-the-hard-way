
# import collections
# stack = collections.deque()

# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# print(stack.pop())
# print(stack[-1])

########################
import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
# print(stack[-1])
print(stack.get())