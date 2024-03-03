vegetables_kg = float(input())
fruits_kg = float(input())
vegetables_total_kgs = int(input())
fruits_total_kgs = int(input())

euro = 1.94

total_profit = ((vegetables_kg * vegetables_total_kgs) + (fruits_kg * fruits_total_kgs)) / euro

print(f"{total_profit:.2f}")