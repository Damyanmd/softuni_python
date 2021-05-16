size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(input())
    for y in range(0, size):
        matrix[x][y] = line[y]

def is_valid_bound(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False

def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills

removed_counter = 0
while True:
    max_kills = 0
    killer_position = []

    for row_index in range(size):
        for column_index in range(size):
            if matrix[row_index][column_index] == 'K':
                kills = calculate_kills(matrix, row_index, column_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, column_index]
    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_counter += 1
    else:
        break
print(removed_counter)