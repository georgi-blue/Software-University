price_ratings = input().split(", ")
entry_point = input()
type_of_item = input()

index = int(entry_point)

left_list = price_ratings[0:index]
right_list = price_ratings[index + 1:len(price_ratings)]

left_sum = 0
right_sum = 0

entry_item = price_ratings[index]

for number in left_list:
    current_number = int(number)

    if type_of_item == "cheap":
        if current_number < int(entry_item):
            left_sum += current_number

    elif type_of_item == "expensive":
        if current_number >= int(entry_item):
            left_sum += current_number


for n in right_list:
    current_n = int(n)

    if type_of_item == "cheap":
        if current_n < int(entry_item):
            right_sum += current_n

    elif type_of_item == "expensive":
        if current_n >= int(entry_item):
            right_sum +=  current_n

if left_sum >= right_sum:
    print(f"Left - {left_sum}")

else:
    print(f"Right - {right_sum}")







