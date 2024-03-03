number = int(input())

combination_counter = 0

for num1 in range (number + 1):
    for num2 in range (number + 1):
        for num3 in range (number + 1):
            if num1 + num2 + num3 == number:
                combination_counter += 1

print(combination_counter)