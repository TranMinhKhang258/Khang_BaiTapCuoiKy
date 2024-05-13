class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, trainghia=None):
        hash_key = self._bam(tu)
        if hash_key not in self.dictionary:
            self.dictionary[hash_key] = {'tu': tu, 'dongnghia': set(), 'trainghia': set()}
        if dongnghia:
            self.dictionary[hash_key]['dongnghia'].add(dongnghia)
        if trainghia:
            self.dictionary[hash_key]['trainghia'].add(trainghia)

    def TraTu(self, tu):
        hash_key = self._bam(tu)
        if hash_key in self.dictionary:
            return self.dictionary[hash_key]['dongnghia'], self.dictionary[hash_key]['trainghia']
        else:
            return None, None

    def _bam(self, tu):
        return tu[0].lower()

# Sử dụng lớp TuDien
td = TuDien()

# Thêm từ vào từ điển
td.NhapTu("tốt", "giỏi", "xấu")
td.NhapTu("đẹp", "xinh đẹp", "xấu xí")
td.NhapTu("hạnh phúc", "vui vẻ", "buồn bã")

# Tra từ trong từ điển
tu_dongnghia, tu_trainghia = td.TraTu("tốt")
print("Từ đồng nghĩa của 'tốt':", tu_dongnghia)
print("Từ trái nghĩa của 'tốt':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("đẹp")
print("Từ đồng nghĩa của 'đẹp':", tu_dongnghia)
print("Từ trái nghĩa của 'đẹp':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("không có")
print("Từ đồng nghĩa của 'không có':", tu_dongnghia)
print("Từ trái nghĩa của 'không có':", tu_trainghia)
