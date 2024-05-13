def DayConDauTien(a, b):
    c = []
    for i in range(len(a)):
        if a[i] in b:
            subsequence = [a[i]]
            j = i + 1
            k = b.index(a[i]) + 1
            while j < len(a) and k < len(b) and a[j] == b[k]:
                subsequence.append(a[j])
                j += 1
                k += 1
            if len(subsequence) > len(c):
                c = subsequence
    return c

a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 3, 6, 2, 5, 3, 7, 8]

print("Dãy con chung đầu tiên của a và b:", DayConDauTien(a, b))
