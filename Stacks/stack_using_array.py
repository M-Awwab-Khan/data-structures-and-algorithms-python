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
    
    def is_empty(self):
        return not bool(self.array)
    
    def __str__(self):
        if self.array:
            res = ''
            for element in self.array[::-1]:
                res += f"{element}\n"
            return res
        return 'Stack is empty'
    
'''Stacks can be implemented in Python in two more ways.
1. Using the 'deque' class from 'collections' module. Same methods used in lists, append and pop are used in deques
2. Using 'LifoQueue' from the 'queue' module . 'put()' and 'get()' methods are used for pushing and popping. It comes with some other useful metjods async well. 
'''
    