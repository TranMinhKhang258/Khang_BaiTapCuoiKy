class DoThi:
    def __init__(self):
        self.dinh = {}  # Dictionary để lưu trữ cặp (đỉnh, danh sách các đỉnh kề)

    def ThemDinh(self, v):
        if v not in self.dinh:
            self.dinh[v] = []

    def ThemCung(self, u, v):
        if u in self.dinh and v in self.dinh:
            self.dinh[u].append(v)
            self.dinh[v].append(u)  # Đối với đồ thị vô hướng, cần thêm cả hai chiều
        else:
            print("Ít nhất một trong các đỉnh", u, "hoặc", v, "không tồn tại trong đồ thị")

    def DuongDi(self, v1, v2):
        visited = set()  # Set để lưu trữ các đỉnh đã được duyệt
        queue = [v1]     # Queue để duyệt theo chiều rộng
        
        while queue:
            node = queue.pop(0)
            if node == v2:
                return True  # Nếu tìm thấy đỉnh v2, có đường đi từ v1 đến v2
            visited.add(node)
            for neighbor in self.dinh[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False  # Nếu không tìm thấy đường đi từ v1 đến v2

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemDinh(4)
dt.ThemCung(1, 2)
dt.ThemCung(2, 3)
dt.ThemCung(3, 4)

print(dt.DuongDi(1, 4))  # Kiểm tra xem có đường đi từ 1 đến 4 không
