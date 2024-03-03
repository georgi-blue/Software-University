rows = int(input())

even_matrix = []

for i in range(rows):
    data = [int(el) for el in input().split(", ")if int(el) % 2 == 0]
    even_matrix.append(data)

print(even_matrix)

