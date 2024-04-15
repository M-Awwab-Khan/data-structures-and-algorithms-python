from node import Node

class Stack:
    def __init__(self):
        self.top: Node = None
        self.bottom: Node = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    