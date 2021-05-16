size = int(input())
matrix = [[0] * size for row in range(0, size)]

def is_not_a_bomb(bombs, hit_row, hit_col):
    for index in range(len(bombs)):
        bomb = all_bombs[index]
        row_bomb, column_bomb = list(map(int, bomb.split(',')))
        if row_bomb == hit_row and column_bomb == hit_col:
            return False
    return True

def is_valid(row, col, matrix):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] > 0 and is_not_a_bomb(all_bombs, row, col):
        return True
    return False

def hitting_targets(row, column, matrix):
    rows = [0, 0, 1, -1, -1, -1, 1, 1]
    cols = [-1, 1, 0, 0, -1, 1, -1, 1]
    for index in range(len(rows)):
        potential_row_hit = row + rows[index]
        potential_col_hit = column + cols[index]
        if is_valid(potential_row_hit, potential_col_hit, matrix):
            matrix[potential_row_hit][potential_col_hit] -= matrix[row][column]
    matrix[row][column] = 0
    return

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

all_bombs = input().split()
for index in range(len(all_bombs)):
    bomb = all_bombs[index]
    row_bomb, column_bomb = list(map(int, bomb.split(',')))
    hitting_targets(row_bomb, column_bomb, matrix)


count = 0
sum_numbers = 0
for list in matrix:
    count += len([i for i in list if i > 0])
    sum_numbers += sum([i for i in list if i > 0])
print(f'Alive cells: {count}')
print(f'Sum: {sum_numbers}')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
