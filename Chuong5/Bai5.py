class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def KiemTraBST(self):
        return self._KiemTraBST(self.root, float('-inf'), float('inf'))

    def _KiemTraBST(self, node, min_val, max_val):
        if node is None:
            return True
        if node.info <= min_val or node.info >= max_val:
            return False
        return (self._KiemTraBST(node.left, min_val, node.info) and 
                self._KiemTraBST(node.right, node.info, max_val))

# Tạo một cây nhị phân ví dụ không phải là BST
tree = CayNhiPhan()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

# Kiểm tra xem cây có phải là BST không và in kết quả
print("Cây là BST: ", tree.KiemTraBST())
