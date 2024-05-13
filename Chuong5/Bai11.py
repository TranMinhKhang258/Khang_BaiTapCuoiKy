class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isSequentialSearchTree(self, root):
        if root is None:
            return True
        if root.left and root.right:
            return False
        return self.isSequentialSearchTree(root.left) and self.isSequentialSearchTree(root.right)

    def BSTTuanTu(self):
        return self.isSequentialSearchTree(self.root)

tree = BinaryTree()
tree.root = TreeNode(4)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(5)
tree.root.left.left = TreeNode(1)
tree.root.left.right = TreeNode(3)
tree.root.right.right = TreeNode(6)

if tree.BSTTuanTu():
    print("Cây là cây BST tìm kiếm tuần tự")
else:
    print("Cây không phải là cây BST tìm kiếm tuần tự")
