class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        self.albums[ten_album] = danh_sach_bai_hat

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            print(f"Thông tin của album '{ten_album}':")
            for i, bai_hat in enumerate(self.albums[ten_album], 1):
                print(f"Bài hát {i}:")
                print(f"  - Tên bài hát: {bai_hat['ten_bai_hat']}")
                print(f"  - Nhạc sĩ sáng tác: {bai_hat['nhac_si']}")
                print(f"  - Ca sĩ: {bai_hat['ca_si']}")
        else:
            print(f"Album '{ten_album}' không tồn tại trong từ điển.")

# Sử dụng lớp TuDien
td = TuDien()

# Thêm thông tin của các album
td.NhapAlbum("Những bài hát của Bức Tường", [
    {"ten_bai_hat": "Những đồi hoa sim", "nhac_si": "Đào Trọng Qúy", "ca_si": "Bức Tường"},
    {"ten_bai_hat": "Bài ca không quên", "nhac_si": "Đào Trọng Qúy", "ca_si": "Bức Tường"},
    {"ten_bai_hat": "Hạt cát", "nhac_si": "Nguyễn Hải Phong", "ca_si": "Bức Tường"}
])

td.NhapAlbum("Album Đừng để ý đến đói của Vũ Cát Tường", [
    {"ten_bai_hat": "Đừng để ý đến đói", "nhac_si": "Vũ Cát Tường", "ca_si": "Vũ Cát Tường"},
    {"ten_bai_hat": "Giấc mơ tôi", "nhac_si": "Vũ Cát Tường", "ca_si": "Vũ Cát Tường"},
    {"ten_bai_hat": "Có khi", "nhac_si": "Vũ Cát Tường", "ca_si": "Vũ Cát Tường"}
])

# Xem thông tin của các album
td.XemAlbum("Những bài hát của Bức Tường")
td.XemAlbum("Album Đừng để ý đến đói của Vũ Cát Tường")
td.XemAlbum("Album không tồn tại")
