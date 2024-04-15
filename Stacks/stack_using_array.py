class Stack:
    def __init__(self):
        self.array = []

    def peak(self):
        if self.array:
            return self.array[-1]
        return 'Stack is empty'
    
    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.array:
            self.array.pop()
        return 'Stack is empty'
    

    