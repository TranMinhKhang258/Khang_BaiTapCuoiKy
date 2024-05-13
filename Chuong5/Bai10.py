class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isBalanced(self, root):
        if root is None:
            return True
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def getHeight(self, node):
        if node is None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def CanBangHoanToan(self):
        return self.isBalanced(self.root)

tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)

if tree.CanBangHoanToan():
    print("Cây là cây cân bằng hoàn toàn")
else:
    print("Cây không phải là cây cân bằng hoàn toàn")
