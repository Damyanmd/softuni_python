rows, cols = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    lines = [str(x) for x in input().split()]
    matrix.append(lines)


command = input()
while command != 'END':
    is_valid = True
    command = command.split()
    try:
        swapping_numbers = [int(x) for x in command[1::]]
    except:
        print('Invalid input!')
        command = input()
        continue
    if command[0] == 'swap' and len(swapping_numbers) == 4:
        column_swapping_numbers = [int(swapping_numbers[x]) for x in range(1, len(swapping_numbers), 2)]
        row_swapping_numbers = [int(swapping_numbers[x]) for x in range(0, len(swapping_numbers), 2)]
        for number in row_swapping_numbers:
            if 0 <= number < rows:
                continue
            else:
                print('Invalid input!')
                is_valid = False
                break
        if is_valid:
            for number in column_swapping_numbers:
                if 0 <= number < cols:
                    continue
                else:
                    print('Invalid input!')
                    is_valid = False
                    break
            if is_valid:
                temp = matrix[swapping_numbers[2]][swapping_numbers[3]]
                matrix[swapping_numbers[2]][swapping_numbers[3]] = matrix[swapping_numbers[0]][swapping_numbers[1]]
                matrix[swapping_numbers[0]][swapping_numbers[1]] = temp
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        print(matrix[i][j], end=" ")
                    print()
    else:
        print('Invalid input!')
    command = input()