vacation_price = float(input())
balance = float(input())

days_counter = 0
total_days = 0

while days_counter < 5:
    action = input()  # spend or save
    money = float(input())

    total_days += 1

    if action == "spend":
        days_counter += 1
        balance = balance - money if balance > money else 0
    else:
        balance += money
        days_counter = 0

    if balance >= vacation_price:
        print(f"You saved the money for {total_days} days.")
        break

else:
    print("You can't save the money.")
    print(total_days)
