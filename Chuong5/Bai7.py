class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def Chep(self):
        return self._Chep(self.root)

    def _Chep(self, node):
        if node is None:
            return None
        
        new_node = Node(node.info)
        new_node.left = self._Chep(node.left)
        new_node.right = self._Chep(node.right)
        
        return new_node

tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

copied_tree = CayNhiPhan()
copied_tree.root = tree.Chep()

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.info, end=" ")
        in_order_traversal(node.right)

print("Cây sao chép:")
in_order_traversal(copied_tree.root)
