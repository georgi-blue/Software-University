rows,columns = [int(el) for el in input().split(", ")]

matrix = []

total_sum = 0

for i in range(rows):
    data = [int(el) for el in input().split(", ")]
    total_sum += sum(data)
    matrix.append(data)

print(total_sum)
print(matrix)


