class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoSanh(self, cay2):
        return self._SoSanh(self.root, cay2.root)

    def _SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            return (node1.info == node2.info and 
                    self._SoSanh(node1.left, node2.left) and 
                    self._SoSanh(node1.right, node2.right))

cay1 = CayNhiPhan()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)
cay1.root.left.left = Node(4)
cay1.root.left.right = Node(5)

cay2 = CayNhiPhan()
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)
cay2.root.left.left = Node(4)
cay2.root.left.right = Node(5)

print("Hai cây giống nhau: ", cay1.SoSanh(cay2))
