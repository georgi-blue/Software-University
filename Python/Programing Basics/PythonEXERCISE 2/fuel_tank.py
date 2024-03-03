type_fuel = input()
fuel_literes = float(input())

if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    if fuel_literes >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")