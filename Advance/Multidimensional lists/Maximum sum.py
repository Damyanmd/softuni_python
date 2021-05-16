rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)

def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum

submatrix_size = 3

best_row_index = 0
best_column_index = 0
best_sum = get_sum_of_submatrix(matrix, best_row_index, best_column_index, submatrix_size)

for row_index in range(len(matrix) - submatrix_size + 1):
    for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
        current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
        if best_sum < current_sum:
            best_sum = current_sum
            best_row_index = row_index
            best_column_index = col_index

print(f'Sum = {best_sum}')
print(f'{matrix[best_row_index][best_column_index]} {matrix[best_row_index][best_column_index + 1]} {matrix[best_row_index][best_column_index + 2]}')
print(f'{matrix[best_row_index + 1][best_column_index]} {matrix[best_row_index + 1][best_column_index + 1]} {matrix[best_row_index + 1][best_column_index + 2]}')
print(f'{matrix[best_row_index + 2][best_column_index]} {matrix[best_row_index + 2][best_column_index + 1]} {matrix[best_row_index + 2][best_column_index + 2]}')
