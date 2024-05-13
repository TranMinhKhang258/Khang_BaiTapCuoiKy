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

    def SoCungVao(self, v):
        socung_vao = 0
        for node in self.dinh:
            for neighbor in self.dinh[node]:
                if neighbor == v:
                    socung_vao += 1
        return socung_vao

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemCung(1, 2)
dt.ThemCung(3, 2)
dt.ThemCung(4, 2)

print(dt.SoCungVao(2))  # In ra số cung đi vào đỉnh 2
