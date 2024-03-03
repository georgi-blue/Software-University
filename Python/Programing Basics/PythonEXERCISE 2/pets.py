from math import ceil
from math import floor

days_count = int(input())
lefted_food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_kg = float(input()) / 1000

dog_needed_food = days_count * dog_food_per_day_kg
cat_needed_food = days_count * cat_food_per_day_kg
turtle_needed_food = days_count * turtle_food_per_day_kg

total_food = dog_needed_food + cat_needed_food + turtle_needed_food

if lefted_food_kg > total_food:
    print(f"{floor(lefted_food_kg - total_food)} kilos of food left.")
else:
    print(f"{ceil(abs(lefted_food_kg - total_food))} more kilos of food are needed.")




