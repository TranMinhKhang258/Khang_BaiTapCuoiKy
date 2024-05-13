class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None
    
    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.Head is None:
            self.Head = new_node
            new_node.KeTiep = new_node  
        else:
            current = self.Head
            while current.KeTiep != self.Head:
                current = current.KeTiep
            current.KeTiep = new_node
            new_node.KeTiep = self.Head

    def RutGon(self):
        if self.Head is None:
            print("Da thuc rong")
            return

        current1 = self.Head
        while True:
            current2 = current1.KeTiep
            while current2 != self.Head:
                if current2.SoMu == current1.SoMu:
                    current1.HeSo += current2.HeSo
                    temp = current2.KeTiep
                    if current2 == self.Head:
                        self.Head = temp
                    del current2
                    current2 = temp
                else:
                    current2 = current2.KeTiep
            next_node = current1.KeTiep
            if current1.HeSo == 0:
                if current1 == self.Head:
                    while next_node.KeTiep != self.Head:
                        next_node = next_node.KeTiep
                    self.Head = next_node.KeTiep
                else:
                    previous.KeTiep = next_node
                del current1
            previous = current1
            current1 = next_node
            if current1 == self.Head:
                break

    def Cong(self, dathuc2):
        result = DaThuc()

        current1 = self.Head
        while current1 is not None:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.KeTiep

        current2 = dathuc2.Head
        while current2 is not None:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.KeTiep

        result.RutGon()

        return result

    def InDaThuc(self):
        if self.Head is None:
            print("Da thuc rong")
            return
        current = self.Head
        while True:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
            if current == self.Head:
                break
            else:
                print("+", end=" ")
        print()

dathuc1 = DaThuc()
dathuc1.Them(3, 2)
dathuc1.Them(4, 3)
dathuc1.Them(2, 1)

dathuc2 = DaThuc()
dathuc2.Them(2, 2)
dathuc2.Them(5, 4)

print("Da thuc 1:")
dathuc1.InDaThuc() 
print("Da thuc 2:")
dathuc2.InDaThuc()  

dathuc3 = dathuc1.Cong(dathuc2)
print("Tong cua Da thuc 1 va Da thuc 2:")
dathuc3.InDaThuc()  
