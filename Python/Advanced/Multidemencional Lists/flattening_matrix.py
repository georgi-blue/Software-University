rows = int(input())

flatted_matrix = []

for i in range(rows):
    nums = [int(el) for el in input().split(", ")]
    for j in nums:
        flatted_matrix.append(j)

print(flatted_matrix)