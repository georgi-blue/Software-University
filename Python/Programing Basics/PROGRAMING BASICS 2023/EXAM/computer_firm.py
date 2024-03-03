n_computers = int(input())

total_maked_sales = 0
total_rating_counter = 0
rating_sum = 0

for _ in range(n_computers):
    computer_model = input()
    total_sales = 0

    rating = int(computer_model[2])
    sales = int(computer_model[:2])

    if rating == 2:
        total_sales = sales * 0
    elif rating == 3:
        total_sales = sales * 0.5
    elif rating == 4:
        total_sales = sales * 0.7
    elif rating == 5:
        total_sales = sales * 0.85
    elif rating == 6:
        total_sales = sales

    total_maked_sales += total_sales
    total_rating_counter += 1
    rating_sum += rating

print(f"{total_maked_sales:.2f}")
print(f"{rating_sum / total_rating_counter:.2f}")





