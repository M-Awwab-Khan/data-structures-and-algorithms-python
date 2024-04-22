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
        
    def delete(self, data):
        if self.root is None:
            return 'Tree is Empty'
        else:
            current_node = self.root
            parent_node = None
            while current_node:
                if data > current_node.data:
                    parent_node = current_node
                    current_node = current_node.right
                elif data < current_node.data:
                    parent_node = current_node
                    current_node = current_node.left
                else:
                    # current node has no child
                    if current_node.left == None and current_node.right == None:
                        if parent_node == None:
                            self.root = None
                            self.number_of_nodes -= 1
                            return
                        elif parent_node.left.data == data:
                            parent_node.left = None
                            self.number_of_nodes -= 1
                            return
                        else:
                            parent_node.right = None
                            self.number_of_nodes -= 1
                            return
                    # current node has one child
                    elif (current_node.left == None) ^ (current_node.right == None):
                        if parent_node == None:
                            if current_node.left:
                                self.root = current_node.left
                                self.number_of_nodes -= 1
                                return
                            else:
                                self.root = current_node.right
                                self.number_of_nodes -= 1
                                return
                        elif parent_node.left.data == data:
                            if current_node.left:
                                parent_node.left = current_node.left
                                current_node.left = None
                                self.number_of_nodes -= 1
                                return
                            else:
                                parent_node.left = current_node.right
                                current_node.right = None
                                self.number_of_nodes -= 1
                                return
                        else:
                            if current_node.left:
                                parent_node.right = current_node.left
                                current_node.left = None
                                self.number_of_nodes -= 1
                                return
                            else:
                                parent_node.right = current_node.right
                                current_node.right = None
                                self.number_of_nodes -= 1
                                return
                    # current node has 2 children
                    else:
                        successor_parent = current_node
                        successor = current_node.right
                        while successor.left:
                            successor_parent = successor
                            successor = successor.left
                        if successor.right == None:
                            current_node.data = successor.data
                            successor_parent.left = None
                            self.number_of_nodes -= 1
                            return
                        else:
                            current_node.data = successor.data
                            successor_parent.left = successor.right
                            self.number_of_nodes -= 1
                            return
        return 'Not Found'


    
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



