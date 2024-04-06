from node import Node   

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = self.head

    def __len__(self) -> int:
        return self.size

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head = new_node
            self.tail = self.head
            self.size = 1

    def prepend(self, data) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        else:
            self.head = new_node
            self.tail = self.head
            self.length = 1

    def insert(self, position, data) -> None:
        new_node = Node(data)
        if position > self.size:
            print('Position out of bound')

        elif position == self.size:
            self.append(data)

        elif position == 0:
            self.prepend(data)

        else:
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.size += 1

    def __str__(self):
        string = 'LinkedList(['
        if self.head:
            current_node = self.head
            while current_node:
                string += f"{current_node.value}, "
                current_node = current_node.next

        string += '])'
        return string
