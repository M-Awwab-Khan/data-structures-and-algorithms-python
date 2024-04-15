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
    
    

    