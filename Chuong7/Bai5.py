class DoThiVoHuong:
    def __init__(self):
        self.dinh = {}  # Dictionary để lưu trữ cặp (đỉnh, danh sách các đỉnh kề)

    def ThemDinh(self, v):
        if v not in self.dinh:
            self.dinh[v] = []

    def ThemCung(self, u, v):
        if u in self.dinh and v in self.dinh:
            self.dinh[u].append(v)
            self.dinh[v].append(u)  # Thêm cả hai chiều cho đồ thị vô hướng
        else:
            print("Ít nhất một trong các đỉnh", u, "hoặc", v, "không tồn tại trong đồ thị")

    def BacDinh(self, v):
        if v in self.dinh:
            return len(self.dinh[v])  # Số cạnh nối với đỉnh v
        else:
            return "Đỉnh không tồn tại trong đồ thị"

# Sử dụng
dt = DoThiVoHuong()
dt.ThemDinh(1)
dt.ThemDinh(2)
dt.ThemDinh(3)
dt.ThemDinh(4)
dt.ThemCung(1, 2)
dt.ThemCung(2, 3)
dt.ThemCung(3, 4)
dt.ThemCung(1, 4)

print(dt.BacDinh(1))  # In ra bậc của đỉnh 1
