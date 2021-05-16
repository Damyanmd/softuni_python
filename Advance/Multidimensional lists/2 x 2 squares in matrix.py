rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    lines = [str(x) for x in input().split()]
    matrix.append(lines)

def get_count_of_same_matrix(matrix, row_index, column_index, size):
    symbol = matrix[row_index][col_index]
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            if matrix[r][c] != symbol:
                return 0
    return 1

sum_counts = 0

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        if matrix[row_index][col_index] == matrix[row_index + 1][col_index + 1]:
            checker_for_B = get_count_of_same_matrix(matrix, row_index, col_index, 2)
            sum_counts += checker_for_B
print(sum_counts)
