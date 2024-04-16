#Queues are another form of linear data structure very similar to stacks.
#The difference is queues follow the FIFO rule - First In First Out, much like real life queues,
#Where the person gets in first, gets to leave first.
#Queues can be implemented with both arrays and linked lists but the array implementation is not eficient
#Because for removing an element from the queues, which happens from the front of the array(queue),
#the indices of the array have to be updated every time, essentially making it an O(n) operation,
#Whereas the same operation can be done in O(1) time with linked lists.
#Queues have enqueue and dequeue operations which correspond to the push and pop operations of stacks , only difference being dequeue removes element from the front
#Time complexities are as follows:
#Peek - O(1)
#Enqueue - O(1)
#Dequeue - O(1)

from node import Node
class Queue:
    #The 'first' pointer will always point to the front of the queue, the element which is to be removed next that is
    #The 'last' pointer will always point to the end of the queue, i.e., the element which has last been entered
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data


    def enqueue(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.first = new_node
        
        else:
            new_node.next = self.last
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.last is None:
            return 'Queue is Empty'
    
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        self.length -= 1
