type_flower = input()
flower_count = int(input())
budget = int(input())

total_price = 0

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.8
TULIPS_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

if type_flower == "Roses":
    total_price = flower_count * ROSES_PRICE

    if flower_count > 80:
        total_price *= 0.90

elif type_flower == "Dahlias":
    total_price = flower_count * DAHLIAS_PRICE

    if flower_count > 90:
        total_price *= 0.85

elif type_flower == "Tulips":
    total_price = flower_count * TULIPS_PRICE

    if flower_count > 80:
        total_price *= 0.85

elif type_flower == "Narcissus":
    total_price = flower_count * NARCISSUS_PRICE

    if flower_count < 120:
        total_price = total_price + (total_price * 0.15)

elif type_flower == "Gladiolus":
    total_price = flower_count * GLADIOLUS_PRICE

    if flower_count < 80:
        total_price = total_price + (total_price * 0.2)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {type_flower} and {budget - total_price:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")