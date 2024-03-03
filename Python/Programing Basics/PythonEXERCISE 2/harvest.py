import math

x_meters_loze = int(input())
y_grozde_kv_m = float(input())
z_leters_wine = int(input())
workers_count = int(input())

total_meters = x_meters_loze * y_grozde_kv_m
wine = (total_meters * 0.4) / 2.5

if wine < z_leters_wine:
    print(f"It will be a tough winter! More {math.floor(abs(wine - z_leters_wine))} liters wine needed.")

elif wine >= z_leters_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.\n"
          f"{math.ceil(wine - z_leters_wine)} liters left -> {math.ceil((wine - z_leters_wine) / workers_count)} liters per person.")
