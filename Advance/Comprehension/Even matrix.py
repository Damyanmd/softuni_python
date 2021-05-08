size = int(input())
matrix = [[] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split(', ')))
    matrix[x] = [line[x] for x in range(len(line)) if line[x] % 2 == 0]

print(matrix)