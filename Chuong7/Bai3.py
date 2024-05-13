class DoThi:
    def __init__(self):
        self.dinh = {}  # Dictionary để lưu trữ cặp (đỉnh, danh sách các đỉnh kề)

    def ThemDinh(self, v):
        if v not in self.dinh:
            self.dinh[v] = []

    def ThemCung(self, u, v):
        if u in self.dinh and v in self.dinh:
            self.dinh[u].append(v)  # Thêm cung từ u đến v
        else:
            print("Ít nhất một trong các đỉnh", u, "hoặc", v, "không tồn tại trong đồ thị")

    def ChuTrinh(self):
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in self.dinh[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for node in self.dinh:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemDinh(4)
dt.ThemCung(1, 2)
dt.ThemCung(2, 3)
dt.ThemCung(3, 4)

print(dt.ChuTrinh())  # Kiểm tra xem đồ thị có chu trình hay không
