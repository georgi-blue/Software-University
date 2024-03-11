n_computers = int(input())  ## user input (whole) number.

total_maked_sales = 0
total_rating_counter = 0
rating_sum = 0

for _ in range(n_computers): ## every iteration is a new computer
    computer_model = input() ## new computer
    total_sales = 0

    rating = int(computer_model[2]) ## getting index (2)
    sales = int(computer_model[:2]) ## getting sliced index to index 2 - (0,1)

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

    total_maked_sales += total_sales    ## adding the current sales to all sales
    total_rating_counter += 1     ## adding the rating
    rating_sum += rating      ## sum the rating

print(f"{total_maked_sales:.2f}")
print(f"{rating_sum / total_rating_counter:.2f}")





