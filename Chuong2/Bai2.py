def TamGiacTren(matrix):
    if len(matrix) != len(matrix[0]): # Kiểm tra xem có phải ma trận vuông hay không
        return False
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n): 
            if matrix[i][j] != 0:
                return False
    return True

matrix = [
    [1, 0, 0],
    [3, 4, 0],
    [4, 5, 6]
]

if TamGiacTren(matrix):
    print("Ma trận là ma trận tam giác trên")
else:
    print("Ma trận không phải là ma trận tam giác trên")
