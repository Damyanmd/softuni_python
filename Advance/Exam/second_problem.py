matrix = [[0] * 5 for row in range(0, 5)]

for x in range(0, 5):
    line = input().split()
    for y in range(0, 5):
        matrix[x][y] = line[y]

def count_targets(matrix):
    count = 0
    for row_index in range(5):
        for column_index in range(5):
            if matrix[row_index][column_index] == 'x':
                count += 1
    return count

def targets_available(matrix):
    for row_index in range(5):
        for column_index in range(5):
            if matrix[row_index][column_index] == 'x':
                return True
    return False

def find_position(matrix):
    for x in range(0, 5):
        for y in range(0, 5):
            if matrix[x][y] == 'A':
                position = [x, y]
                return position

def move(matrix, direction, steps):
    position = find_position(matrix)
    if direction == 'right':
        for i in range(1, steps + 1):
            if position[1] + i == 5 or matrix[position[0]][position[1] + i] != '.':
                return
        matrix[position[0]][position[1]] = '.'
        matrix[position[0]][position[1] + steps] = 'A'

    elif direction == 'left':
        for i in range(1, steps + 1):
            if 0 > position[1] - i or matrix[position[0]][position[1] - i] != '.':
                return
        matrix[position[0]][position[1]] = '.'
        matrix[position[0]][position[1] - steps] = 'A'

    elif direction == 'down':
        for i in range(1, steps + 1):
            if position[0] + i == 5 or matrix[position[0] + i ][position[1]] != '.':
                return
        matrix[position[0]][position[1]] = '.'
        matrix[position[0] + steps][position[1]] = 'A'

    elif direction == 'up':
        for i in range(1, steps + 1):
            if 0 > position[0] - i or matrix[position[0] - i][position[1]] != '.':
                return
        matrix[position[0]][position[1]] = '.'
        matrix[position[0] - steps][position[1]] = 'A'

def shoot(matrix, direction):
    position = find_position(matrix)
    if direction == 'right':
        for s in range(position[1], 5):
            if matrix[position[0]][s] == 'x':
                matrix[position[0]][s] = '.'
                hit = [position[0], s]
                return hit
        return None

    elif direction == 'left':
        for s in range(position[1], 0, -1):
            if matrix[position[0]][s] == 'x':
                matrix[position[0]][s] = '.'
                hit = [position[0], s]
                return hit
        return None

    elif direction == 'down':
        for s in range(position[0], 5):
            if matrix[s][position[1]] == 'x':
                matrix[s][position[1]] = '.'
                hit = [s, position[1]]
                return hit
        return None

    elif direction == 'up':
        for s in range(position[1], 0, -1):
            if matrix[s][position[1]] == 'x':
                matrix[s][position[1]] = '.'
                hit = [s, position[1]]
                return hit
        return None

max_kills = 0
hit_targets = []
count = int(input())

for _ in range(count):
    data = input().split()

    if data[0] == 'move':
        move(matrix, data[1], int(data[2]))
    elif data[0] == 'shoot':
        is_hit = shoot(matrix, data[1])
        if is_hit:
            hit_targets.append(is_hit)
            max_kills += 1

    if not targets_available(matrix):
        break

if not targets_available(matrix):
    print(f'Training completed! All {max_kills} targets hit.')
    for i in hit_targets:
        print(i)
else:
    print(f'Training not completed! {count_targets(matrix)} targets left.')
    for i in hit_targets:
        print(i)