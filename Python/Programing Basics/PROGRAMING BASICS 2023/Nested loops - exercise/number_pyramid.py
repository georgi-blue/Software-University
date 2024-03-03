n = int(input())
counter = 0

for rows in range (1, n + 1):
    for columns in range (1, rows + 1):
        counter += 1

        if rows != columns:
            print(counter, end=" ")
        else:
            print(counter)

        if counter == n:
            exit()