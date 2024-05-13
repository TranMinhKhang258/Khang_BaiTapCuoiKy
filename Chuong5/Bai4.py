class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan():
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self):
        return self._SoNutTrungGian(self.root) - 1

    def _SoNutTrungGian(self, node):
        if node is None:
            return 0
        elif node.left is not None or node.right is not None:
            return self._SoNutTrungGian(node.left) + self._SoNutTrungGian(node.right) + 1
        else:
            return 0
        
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.right.right.left = Node(7)

print("Số nút trung gian của cây là:", tree.SoNutTrungGian())
        
