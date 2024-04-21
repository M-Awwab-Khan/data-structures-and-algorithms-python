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
        
    def search(self, data):

        if self.root is None:
            return 'Tree is empty'
        else:
            current_node = self.root
            while current_node:
                if current_node.data == data:
                    return 'Value found in the tree'
                elif data > current_node.data:
                    current_node = current_node.right
                elif data < current_node.data:
                    current_node = current_node.left
            return 'Value not found in the tree'


    
    def inorder(self):

        def _inorder(curr):
            if curr:
                _inorder(curr.left)
                print(f"{curr.data} -> ", end=' ')
                _inorder(curr.right)

        _inorder(self.root)
        print()

    def preorder(self):

        def _preorder(curr):
            if curr:
                print(f"{curr.data} -> ", end=' ')
                _preorder(curr.left)
                _preorder(curr.right)

        _preorder(self.root)
        print()

    def postorder(self):

        def _postorder(curr):
            if curr:
                _postorder(curr.left)
                _postorder(curr.right)
                print(f"{curr.data} -> ", end=' ')

        _postorder(self.root)
        print()



