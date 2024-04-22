from node import Node   

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = self.head

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.head is None

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
    
    def insert_after(self, prev_node, data) -> None:
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    def delete_by_value(self, value) -> None:
        if not self.head:
            print("LinkedList is empty. ")
            return
        current_node = self.head
        if current_node.value == value:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            self.size -= 1
            current_node.next = None
            return
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.size -= 1
                if current_node.next == None:
                    self.tail = current_node
                break
            current_node = current_node.next
        else:
            print("Given value is not found. ")

    def delete_by_position(self, position) -> None:
        if position >= self.size:
            print("Position out of bound.")
            return
        if not self.head:
            print("LinkedList is empty. ")
            return
        current_node = self.head
        if position == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            self.size -= 1
            current_node.next = None
            return

        for i in range(position-1):
            current_node = current_node.next
        
        current_node.next = current_node.next.next
        if current_node.next == None:
            self.tail = current_node
        self.size -= 1

    def reverse(self):
        if self.size > 1:
            self.tail = self.head
            prev, current, next_ = None, self.head, self.head.next
            while current:
                next_ = current.next
                current.next = prev
                prev = current
                current = next_
                
            
            self.head = prev

    def search(self, data) -> bool:
        if self.is_empty():
            return False
        current_node = self.head

        while current_node:
            if current_node.value == data:
                return True
            
            current_node = current_node.next
        return False

    def __str__(self):
        string = 'LinkedList(['
        if self.head:
            current_node = self.head
            while current_node:
                string += f"{current_node.value} -> "
                current_node = current_node.next

        string += 'None])'
        return string
