
#This ia popular interview question. Implementation of a queue using stacks.
#We have access to stacks push and pop operations. Using those we need to execute a qeueue's enqueue and dequeue operation
#It can be done in two ways, by either making the enqueue operation costly(O(n)) or the dequeue operation costly(O(n))
#In the first method, we need two stacks say s1 and s2 and we have maintain them such that the element entered first
#Is always at the top of the stack s1. This way, for dequeue, we just need to pop from s1.
#But for enqueueing, we have to make the enqueued item reach the bottom of the stack.
#For that, we will have to pop the elements of s1 one by one and push them onto stack 2, then add the new item to stack1 ,
#And then again pop everything from stack2 and push it back to stack 1., so the new item is now at the last.

#Lets implement a queue using stacks(array implementation) using this method first

class Queue:

    def __init__(self):
        ...
