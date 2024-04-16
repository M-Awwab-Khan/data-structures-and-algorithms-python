#from queue_using_stack import Queue
from queue_using_linkedlist import Queue

queue = Queue()

for i in range(2, 11, 2):
    queue.enqueue(i)


print(queue)

queue.dequeue()
print(queue)

print(queue.peek())
