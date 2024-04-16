from queue_using_stack import Queue

queue = Queue()

for i in range(2, 11, 2):
    queue.enqueue(i)


print(queue)
