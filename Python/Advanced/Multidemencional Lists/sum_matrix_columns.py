rows, col = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

new_matrix = []

for row_index in range(col):
    col_sum = 0
    for col_index in range(rows):
        current_element = matrix[col_index][row_index]
        col_sum += current_element
    new_matrix.append(col_sum)

print(*new_matrix, sep='\n')
