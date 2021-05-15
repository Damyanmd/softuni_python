size = int(input())
matrix = []

for _ in range(size):
    row = [str(x) for x in list(input())]
    matrix.append(row)

symbol = input()
location = []
found = False
for row in range(0, size):
    if found:
        break
    for col in range(0, size):
        if matrix[row][col] == symbol:
            location = [row, col]
            found = True
            break

if found == True:
    print(f"({location[0]}, {location[1]})")
else:
    print(f"{symbol} does not occur in the matrix")