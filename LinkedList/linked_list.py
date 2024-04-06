from node import Node   

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = self.head

    def __len__(self) --> int:
        return self.size

    def append(self, node: Node) -> None:
        if self.head:
            self.tail.next = node
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.tail = self.head
            self.size = 1

    def prepend(self, node: Node) -> None:
        if self.head:
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            self.head = node
            self.tail = self.head
            self.length = 1

    def __str__(self):
        print('LinkedList([', end='')
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data, end=', ')
                current_node = current_node.next

        print('])')
