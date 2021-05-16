size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal_1 = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
sum_diagonal_2 = sum(matrix[i][size - i - 1] for i in range(size))
print(abs(sum_diagonal_1 - sum_diagonal_2))