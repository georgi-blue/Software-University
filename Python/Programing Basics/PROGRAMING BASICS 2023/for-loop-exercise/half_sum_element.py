number_of_lines = int(input())

max_number = float("-inf")
total_sum = 0

for _ in range (number_of_lines):
    number = int(input())

    if number > max_number:
        max_number = number

    total_sum += number

if max_number == total_sum - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - (total_sum - max_number))}")

