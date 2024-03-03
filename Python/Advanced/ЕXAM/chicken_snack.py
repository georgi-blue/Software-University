from collections import deque

personal_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])
food_calculator = 0

while personal_money and food_prices:
    current_money = personal_money[-1]
    current_price = food_prices[0]

    if current_money == current_price:
        food_calculator += 1
    elif current_money > current_price:
        difference = current_money - current_price
        if len(personal_money) > 1:
            personal_money[-1] += difference
        food_calculator += 1

    food_prices.popleft()
    personal_money.pop()

if food_calculator >= 4:
    print(f"Gluttony of the day! Henry ate {food_calculator} foods.")
elif 1 < food_calculator < 4:
    print(f"Henry ate: {food_calculator} foods.")
elif food_calculator == 1:
    print(f"Henry ate: {food_calculator} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")