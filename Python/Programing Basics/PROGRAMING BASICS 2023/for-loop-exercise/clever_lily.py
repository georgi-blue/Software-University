total_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_given = 10
money_from_gifts = 0

for age in range (1, total_age + 1):
    if age % 2 == 0:
        money_from_gifts += money_given - 1
        money_given += 10
    else:
        money_from_gifts += toy_price

if money_from_gifts >= washing_machine_price:
    print(f"Yes! {money_from_gifts - washing_machine_price:.2f}")
else:
    print(f"No! {abs(money_from_gifts - washing_machine_price):.2f}")