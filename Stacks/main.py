# from stack_using_array import Stack
from stack_using_linkedlist import Stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)
stack.pop()

print(stack)
print(stack.peek())

print('element is found at index: ', stack.search(2))