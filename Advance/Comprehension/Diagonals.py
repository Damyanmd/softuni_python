size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split(', ')))
    for y in range(0, size):
        matrix[x][y] = line[y]

diagonal_1 = [matrix[size - i - 1][size - i - 1] for i in range(size)]
diagonal_1.reverse()
diagonal_2 = [matrix[i][size - i - 1] for i in range(size)]
print(f'First diagonal: {", ".join(str(x) for x in diagonal_1)}. Sum: {sum(diagonal_1)}')
print(f'Second diagonal: {", ".join(str(x) for x in diagonal_2)}. Sum: {sum(diagonal_2)}')