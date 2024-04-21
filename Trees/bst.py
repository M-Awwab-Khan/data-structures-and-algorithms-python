from node import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):

        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1

        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return
    
    def inorder(self):

        def _inorder(curr):
            if curr:
                _inorder(curr.left)
                print(f"{curr.data} -> ", end=' ')
                _inorder(curr.right)

        _inorder(self.root)



