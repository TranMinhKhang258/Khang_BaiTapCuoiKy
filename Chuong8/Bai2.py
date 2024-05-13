class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, trainghia=None):
        hash_key = self._bam(tu)
        if hash_key not in self.dictionary:
            self.dictionary[hash_key] = {'tu': tu, 'dongnghia': set(), 'trainghia': set()}
        if dongnghia:
            self.dictionary[hash_key]['dongnghia'].update(dongnghia)
        if trainghia:
            self.dictionary[hash_key]['trainghia'].update(trainghia)

    def DongNghia(self, tu):
        hash_key = self._bam(tu)
        if hash_key in self.dictionary:
            return list(self.dictionary[hash_key]['dongnghia'])
        else:
            return []

    def TraiNghia(self, tu):
        hash_key = self._bam(tu)
        if hash_key in self.dictionary:
            return list(self.dictionary[hash_key]['trainghia'])
        else:
            return []

    def _bam(self, tu):
        return tu[0].lower()

# Sử dụng lớp TuDien
td = TuDien()

# Thêm từ vào từ điển
td.NhapTu("tốt", dongnghia=["tuyệt vời", "ưu tú"], trainghia=["xấu", "tệ"])
td.NhapTu("đẹp", dongnghia=["xinh đẹp", "hấp dẫn"], trainghia=["xấu xí", "kinh khủng"])

# Tra từ trong từ điển
print("Từ đồng nghĩa của 'tốt':", td.DongNghia("tốt"))
print("Từ trái nghĩa của 'tốt':", td.TraiNghia("tốt"))

print("Từ đồng nghĩa của 'đẹp':", td.DongNghia("đẹp"))
print("Từ trái nghĩa của 'đẹp':", td.TraiNghia("đẹp"))

print("Từ đồng nghĩa của 'không có trong từ điển':", td.DongNghia("không có"))
print("Từ trái nghĩa của 'không có trong từ điển':", td.TraiNghia("không có"))
