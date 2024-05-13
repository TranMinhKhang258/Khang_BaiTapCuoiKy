def maxRectangle(matrix):
    if not matrix:
        return 0

    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0

        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

def Dao(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 1 and not visited[x][y]

    def dfs(x, y):
        area = 0
        stack = [(x, y)]

        while stack:
            i, j = stack.pop()
            if is_valid(i, j):
                area += 1
                visited[i][j] = True
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            stack.append((i + dx, j + dy))

        return area

    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not visited[i][j]:
                area = dfs(i, j)
                max_area = max(max_area, area)

    print("Diện tích lớn nhất của các đảo có dạng hình chữ nhật là:", maxRectangle(matrix))

matrix = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0]
]

Dao(matrix)
