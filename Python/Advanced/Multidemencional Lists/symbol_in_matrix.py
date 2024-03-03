n = int(input())

matrix = []

for i in range(n):
    data = [ch for ch in input()]
    matrix.append(data)

searching_element = input()

for row_index in range(n):
    for col_index in range(n):
        current_element = matrix[row_index][col_index]

        if current_element == searching_element:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searching_element} does not occur in the matrix")