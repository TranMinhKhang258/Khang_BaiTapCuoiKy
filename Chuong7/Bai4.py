class DoThi:
    def __init__(self):
        self.dinh = set()  # Set để lưu trữ các đỉnh

    def ThemDinh(self, v):
        self.dinh.add(v)

    def ThemCung(self, u, v):
        self.dinh.add(u)
        self.dinh.add(v)
        # Code để thêm cung vào đồ thị

    def ChuaDinh(self, v):
        return v in self.dinh

# Sử dụng
dt = DoThi()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)

print(dt.ChuaDinh(1))  # Kết quả: True
print(dt.ChuaDinh(4))  # Kết quả: False
