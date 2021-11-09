
def rotate(matrix):
    rotated = []
    width = len(matrix[0])
    height = len(matrix)
    for x in range(width):
        row = []
        for y in range(height):
            row.append(matrix[height - 1 - y][x])
        rotated.append(row)
    return rotated
