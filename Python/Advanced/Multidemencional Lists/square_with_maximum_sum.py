rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split(', ')])


max_sum = float('-inf')

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        under_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        total_sum = current_element + next_element + diagonal_element + under_element

        if total_sum > max_sum:
            max_sum = total_sum
            new_matrix = [[current_element, next_element], [under_element, diagonal_element]]

print(*new_matrix[0])
print(*new_matrix[1])
print(max_sum)


