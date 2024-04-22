from bst import BinarySearchTree

my_bst = BinarySearchTree()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)
print('In order traversal: ', end=' ')
my_bst.inorder()

print('Pre order traversal: ', end= ' ')
my_bst.preorder()

print('Post order traversal: ', end= ' ')
my_bst.postorder()

print(my_bst.search(10))
print(my_bst.search(11))

my_bst.delete(13)
my_bst.inorder()

my_bst.delete(5)
my_bst.inorder()

my_bst.delete(3)
my_bst.inorder()

my_bst.delete(7)
my_bst.inorder()