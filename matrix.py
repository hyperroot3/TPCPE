def zeroMatrix(rows, columns):
    rowEchelon = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        rowEchelon.append(row)
    return rowEchelon

print(zeroMatrix(5, 6))