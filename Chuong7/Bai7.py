class DoThi:
    def __init__(self):
        self.dinh = {}  # Dictionary để lưu trữ cặp (đỉnh, danh sách cung đi ra từ đỉnh)
        self.cung = 0   # Biến để đếm tổng số cung trong đồ thị

    def ThemDinh(self, v):
        if v not in self.dinh:
            self.dinh[v] = []

    def ThemCung(self, u, v):
        if u in self.dinh:
            self.dinh[u].append(v)
            self.cung += 1
        else:
            print("Đỉnh", u, "không tồn tại trong đồ thị")

    def SoCungRa(self, v):
        if v in self.dinh:
            return len(self.dinh[v])
        else:
            return "Đỉnh không tồn tại trong đồ thị"

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemCung(1, 2)
dt.ThemCung(1, 3)

print(dt.SoCungRa(1))  # In ra số cung đi ra từ đỉnh 1
