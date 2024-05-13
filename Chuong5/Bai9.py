class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def CayCon(self, cay2):
        return self._CayCon(self.root, cay2.root)

    def _CayCon(self, node1, node2):
        if node1 is None:
            return False
        if node2 is None:
            return True
        if self._GiongNhau(node1, node2):
            return True
        return self._CayCon(node1.left, node2) or self._CayCon(node1.right, node2)

    def _GiongNhau(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.info == node2.info and 
                self._GiongNhau(node1.left, node2.left) and 
                self._GiongNhau(node1.right, node2.right))

cay1 = CayNhiPhan()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)
cay1.root.left.left = Node(4)
cay1.root.left.right = Node(5)

cay2 = CayNhiPhan()
cay2.root = Node(2)
cay2.root.left = Node(4)
cay2.root.right = Node(5)

print("Cây nhị phân 2 là cây con của cây nhị phân 1:", cay1.CayCon(cay2))
