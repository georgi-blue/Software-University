n_kilometres = int(input())
day_or_night = input()

total_sum = 0

start_price = 0.7
taxi_day = 0.79
taxi_night = 0.9
bus_day_and_night = 0.09
train_day_and_night = 0.06

if 0 < n_kilometres <= 20 and day_or_night == "day":
    total_sum = start_price + n_kilometres * taxi_day

elif 0 < n_kilometres <= 20 and day_or_night == "night":
    total_sum = start_price + n_kilometres * taxi_night

if 20 < n_kilometres < 100:

    if bus_day_and_night > train_day_and_night:
        total_sum = bus_day_and_night * n_kilometres

    elif bus_day_and_night < train_day_and_night:
        total_sum = train_day_and_night * n_kilometres

elif n_kilometres >= 100:
    total_sum = train_day_and_night * n_kilometres

print(f"{total_sum:.2f}")