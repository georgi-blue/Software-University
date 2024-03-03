counter = int(input())

numbers = []
filtered_numbers = []

for number in range(counter):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for current_num in numbers:
        if current_num % 2 == 0:
            filtered_numbers.append(current_num)
        elif current_num == 0:
            filtered_numbers.append(current_num)
elif command == "odd":
    for _ in numbers:
        if _ % 2 == 1:
            filtered_numbers.append(_)
elif command == "negative":
    for i in numbers:
        if i < 0:
            filtered_numbers.append(i)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)


print(filtered_numbers)


