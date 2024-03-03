film_budget = float(input())
statists_number = int(input())
one_statist_clothes_price = float(input())

dekor_price = film_budget / 10
clothes_sum = statists_number * one_statist_clothes_price

if statists_number > 150:
    clothes_sum = clothes_sum - (clothes_sum / 10)

total_sum_film = dekor_price + clothes_sum

if total_sum_film > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(total_sum_film - film_budget):.2f} leva more.")

if total_sum_film <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_sum_film:.2f} leva left.")
