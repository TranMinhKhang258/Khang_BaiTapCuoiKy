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

    def LienThong(self):
        visited = set()
        self.DFS(next(iter(self.dinh)), visited)  # Thực hiện DFS từ một đỉnh bất kỳ

        # Kiểm tra xem tất cả các đỉnh đã được duyệt qua hay không
        return len(visited) == len(self.dinh)

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemCung(1, 2)
dt.ThemCung(2, 3)

print(dt.LienThong())  # Kiểm tra xem đồ thị có liên thông không
