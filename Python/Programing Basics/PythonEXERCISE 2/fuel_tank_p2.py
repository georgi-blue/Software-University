type_fuel = input()
fuel_count = float(input())
club_card = input()

total_sum = 0

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if club_card == "Yes":
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

if type_fuel == "Gas":
    total_sum = fuel_count * gas_price

elif type_fuel == "Gasoline":
    total_sum = fuel_count * gasoline_price

elif type_fuel == "Diesel":
    total_sum = fuel_count * diesel_price

if 20 <= fuel_count <= 25:
    total_sum *= 0.92

elif fuel_count > 25:
    total_sum *= 0.9

print(f"{total_sum:.2f} lv.")