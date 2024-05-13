class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan():
    def __init__(self):
        self.root = None

    def KiemTraAVL(self):
        return self._KiemTraAVL(self.root)

    def _KiemTraAVL(self, node):
        if node is None:
            return 0
        
        left_height = self._KiemTraAVL(node.left)
        right_height = self._KiemTraAVL(node.right)

        if left_height == -1 or right_height == -1:
            return -1
        elif abs(left_height - right_height) > -1:
            return -1
        else:
            return max(left_height, right_height) + 1
        
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.left.left = Node(5)

print("Cây là AVL: ", tree.KiemTraAVL())
        