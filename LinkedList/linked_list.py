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
