deposit = input()

total = 0.0

while deposit != "NoMoreMoney":
    amount = float(deposit)
    if amount < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {amount:.2f}")
        total += amount
        deposit = input()
print(f"Total: {total:.2f}")