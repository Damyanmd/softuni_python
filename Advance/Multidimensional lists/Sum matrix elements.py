rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

sum_matrix = 0
for list in matrix:
    sum_matrix += sum(list)

print(sum_matrix)
print(matrix)