size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

def valid(col, row):
    if 0 <= col < size and 0 <= row < size:
        is_valid = True
    else:
        print('Invalid coordinates')
        is_valid = False
    return is_valid

command = input()
while command != 'END':
    command = command.split()
    try:
        numbers = [int(x) for x in command[1::]]
    except:
        print('Invalid coordinates')
        command = input()
        continue
    if command[0] == 'Add' and len(numbers) == 3:
        column_number = int(numbers[1])
        row_number = int(numbers[0])
        is_valid = valid(column_number, row_number)
        if is_valid:
            matrix[row_number][column_number] += int(numbers[2])
    elif command[0] == 'Subtract' and len(numbers) == 3:
        column_number = int(numbers[1])
        row_number = int(numbers[0])
        is_valid = valid(column_number, row_number)
        if is_valid:
            matrix[row_number][column_number] -= int(numbers[2])
    else:
        print('Invalid coordinates')
    command = input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()