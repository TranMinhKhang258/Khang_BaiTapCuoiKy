class DoThi:
    def __init__(self):
        self.dinh = {}  # Dictionary để lưu trữ cặp (đỉnh, danh sách các đỉnh kề)

    def ThemDinh(self, v):
        if v not in self.dinh:
            self.dinh[v] = []

    def ThemCung(self, u, v):
        if u in self.dinh and v in self.dinh:
            self.dinh[u].append(v)  # Thêm cung từ u đến v
            self.dinh[v].append(u)  # Thêm cung từ v đến u (cho đồ thị vô hướng)
        else:
            print("Ít nhất một trong các đỉnh", u, "hoặc", v, "không tồn tại trong đồ thị")

    def DFS(self, node, visited):
        visited.add(node)
        for neighbor in self.dinh[node]:
            if neighbor not in visited:
                self.DFS(neighbor, visited)

    def SoThanhPhan(self):
        visited = set()
        so_thanh_phan = 0

        for node in self.dinh:
            if node not in visited:
                self.DFS(node, visited)
                so_thanh_phan += 1

        return so_thanh_phan

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemDinh(4)
dt.ThemCung(1, 2)
dt.ThemCung(3, 4)

print(dt.SoThanhPhan())  # In ra số thành phần liên thông của đồ thị
