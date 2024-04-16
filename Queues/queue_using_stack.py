
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
        self.s1 = []
        self.s2 = []

    def peek(self):
        if self.s1:
            return self.s1[-1]
        else:
            return 'Queue is Empty'

    def enqueue(self, data):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())


    def dequeue(self):
        if self.s1:
            return self.s1.pop()

        else:
            return 'Queue is Empty'

    def __str__(self):
        if len(self.s1) == 0:
            return "Queue is Empty"

        res = ''
        for i in range(len(self.s1) - 1,0,-1):
            res += f'{self.s1[i]} <<-- '
        res += str(self.s1[0])

        return res
